import psutil
import cpuinfo

cpu = cpuinfo.get_cpu_info()

print("="*10, " Procesador ", "="*10)
print("Nombre                   :", cpu.get('brand_raw'))
print("Fabricante               :", cpu.get('vendor_id_raw'))
print("Bits                     :", cpu.get('bits'))
print("Núcleos                  :", psutil.cpu_count(logical=False))
print("Threads                  :", psutil.cpu_count(logical=True))
print("Frecuencia de referencia :", cpu.get('hz_advertised_friendly'))
print("Frecuencia actual        :", cpu.get('hz_actual_friendly'))
print("Instrucciones            :", cpu.get('flags'))