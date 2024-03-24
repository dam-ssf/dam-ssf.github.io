import socket
from list_nics import get_nic

ETHER_TYPE = {
    'ip': 0x0806,
    'arp': 0x0800,
    'ipv6': 0x86dd,
    'custom': 0x1234
}

def _mac_as_bytes(mac):
    return bytes.fromhex(mac.replace(':', '').replace('-', ''))

def send_frame(ifname, dest_mac, eth_type, payload):
    src_mac = _mac_as_bytes(get_nic(ifname)['mac'])
    dest_mac = _mac_as_bytes(dest_mac)
    frame = dest_mac + src_mac + eth_type + payload.encode('utf-8')
    s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW)
    s.bind((ifname, 0))
    s.send(frame)
    s.close()

def main():
    # broadcast a packet with 123456 as payload

    send_frame('Wi-Fi', 'FF:FF:FF:FF:FF:FF', ETHER_TYPE['custom'], 'Hola mundo!')

if __name__ == '__main__':
    main()

