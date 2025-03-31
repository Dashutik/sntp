import argparse
import socket


PORT_NUM = 200

def get_time():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.sendto(b'', ('127.0.0.1', PORT_NUM))
        data, _ = sock.recvfrom(1024)
        print(data.decode())

if __name__ == '__main__':
    parser = argparse.ArgumentParser(usage="print python3 {SCRIPT file_name}' to start",
                                     description="A client to get time from server")
    get_time()
