import threading
import pydivert
import os
from datetime import datetime

# Lista para almacenar los mensajes recibidos
mensajes_recibidos = []

# Función para limpiar la pantalla de la terminal
def limpiar_pantalla():
    os.system('cls')

# Función para imprimir los mensajes en la parte superior de la terminal
def imprimir_mensajes():
    limpiar_pantalla()
    print("---- Mensajes Recibidos ----")
    for mensaje in mensajes_recibidos:
        print(f"MAC Origen: {mensaje['mac_origen']} - Fecha y Hora: {mensaje['fecha_hora']} - Mensaje: {mensaje['mensaje']}")
    print("-" * 40)

# Función para capturar frames
def capturar_frames():
    # Inicia la captura de paquetes Ethernet
    with pydivert.WinDivert("inbound") as w:
        for packet in w:
            # Procesa los frames capturados
            print(packet.raw.hex())
            """
            if ethertype == 0x0800:
                mensaje = packet.payload.decode()
                mac_origen = packet.src.decode()
                fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                # Agrega el mensaje recibido a la lista
                mensajes_recibidos.append({'mac_origen': mac_origen, 'fecha_hora': fecha_hora, 'mensaje': mensaje})

                # Imprime los mensajes actualizados
                imprimir_mensajes()
            """

# Convierte la dirección MAC de texto a bytes
def mac_addr(mac):
    return bytes.fromhex(mac.replace(":", ""))

# Función para obtener la dirección MAC de la tarjeta de red
def get_mac():
    with pydivert.WinDivert() as w:
        mac = w.get_adapter_mac()
    return mac

# Función para enviar un mensaje por broadcast
def enviar_mensaje(mac_destino, mensaje):
    # Parámetros del paquete Ethernet
    mac_destino_bytes = mac_addr(mac_destino)
    mac_origen_bytes = mac_addr(get_mac())
    payload_bytes = mensaje.encode()

    # Crea el paquete Ethernet con los parámetros separados
    packet = pydivert.Packet(mac_destino_bytes, mac_origen_bytes, payload=payload_bytes)

    # Envía el paquete
    with pydivert.WinDivert() as w:
        w.send(packet)

    imprimir_mensajes()

# Función principal
def main():
    # Crea y arranca un hilo para capturar frames en segundo plano
    hilo_captura = threading.Thread(target=capturar_frames)
    hilo_captura.daemon = True  # Permite que el hilo se detenga cuando el programa principal se cierre
    hilo_captura.start()

    # Menú principal
    while True:
        limpiar_pantalla()
        print("---- Terminal de Mensajes ----")
        print("Mensajes recibidos se mostrarán aquí.\n")
        print("-" * 40)

        mensaje = input("Ingrese un mensaje para enviar por broadcast (o presione Enter para salir): ")
        if not mensaje:
            break
        else:
            enviar_mensaje("ff:ff:ff:ff:ff:ff", mensaje)

if __name__ == "__main__":
    main()
