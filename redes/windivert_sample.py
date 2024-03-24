import pydivert
from threading import Thread, Event
from pprint import pprint

e = Event()

def handle_packet(name):
    with pydivert.WinDivert("outbound") as w:
        for packet in w:
            pprint(packet)
            w.send(packet)
            if e.is_set():
                break

def main():
    t = Thread(target=handle_packet, args=(1,))
    t.start()
    input('Press Enter to stop')
    e.set()
    t.join()


if __name__ == '__main__':
    main()
