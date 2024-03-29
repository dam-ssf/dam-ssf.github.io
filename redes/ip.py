class IP:

    def __init__(self, ip):
        if not self._check_ip(ip):
            raise ValueError("Dirección IP inválida")
        self.ip = [ int(part) for part in ip.split('.') ]

    def to_bin(self):
        ip_bin = []
        for i in self.ip:
            part = bin(i)[2:]               # [2:] elimina 0b del inicio
            ip_bin.append(part.zfill(8))    # zfill(8) rellena con 0 a la izquierda
        return '.'.join(ip_bin)
    
    def _check_ip(self, ip):
        ip = ip.split('.')
        if len(ip) != 4:
            return False
        for i in ip:
            if not i.isdigit():
                return False
            if not 0 <= int(i) <= 255:
                return False
        return True
    
    def get_network(self, netmask):
        network = []
        for i in range(4):
            ip_part = int(self.ip[i])
            netmask_part = int(netmask.ip[i])
            network.append(str(ip_part & netmask_part))
        return IP('.'.join(network))

    def __str__(self):
        ip_str = []
        for part in self.ip:
            ip_str.append(str(part))
        return '.'.join(ip_str)