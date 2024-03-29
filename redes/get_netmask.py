import sys

def get_netmask(bits):
    if not 0 <= bits <= 32:
        raise ValueError("Número de bits incorrecto")
    netmask = bits * '1' + (32 - bits) * '0'
    netmask = [ str(int(netmask[i:i+8], 2)) for i in range(0, 32, 8) ]
    netmask = '.'.join(netmask)
    return netmask

def main():
    if len(sys.argv) < 2:
        print("Uso: python get_netmask.py <bits>")
        sys.exit(1)
    bits = int(sys.argv[1])
    try:
        netmask = get_netmask(bits)
    except ValueError as e:
        print(e)
        sys.exit(1)
    print(f'Máscara de red: {netmask}')

if __name__ == '__main__':
    main()