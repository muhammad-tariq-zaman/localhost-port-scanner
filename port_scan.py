import socket, sys
def scan(host, ports):
    open_ports = []
    for p in ports:
        s = socket.socket()
        s.settimeout(0.5)
        try:
            if s.connect_ex((host, p)) == 0: open_ports.append(p)
        finally: s.close()
    return open_ports
if __name__ == "__main__":
    host = sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1"
    ports = [int(x) for x in sys.argv[2].split(",")] if len(sys.argv) > 2 else [22, 80, 443, 3389]
    print(f"Open on {host}: {scan(host, ports)}")
