import argparse
import socket
import datetime

PORT_NUM = 200

import subprocess

def check_port(PORT_NUM):
    command = f"netstat -ano | findstr :{PORT_NUM}"
    result = subprocess.run(command, capture_output=True, text=True, shell=True)

    if result.returncode == 0:
        print(f"Результаты для порта {PORT_NUM}:")
        print(result.stdout)
    else:
        print(f"Не удалось выполнить команду. Код возврата: {result.returncode}")


def get_time(offset):
    real_time = datetime.datetime.now()
    return str(real_time + datetime.timedelta(seconds=offset))

def start_server(offset):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.bind(('127.0.0.1', PORT_NUM))
        print("Сервер запущен, ожидает подключения...")
        while True:
            data, addr = sock.recvfrom(1024)
            print(f"Получен запрос от {addr}")
            time = get_time(offset)
            sock.sendto(time.encode('utf-8'), addr)

def get_time_offset():
    with open('config.txt', 'r') as config:
        try:
            return int(config.read())
        except Exception:
            raise Exception("There must be an integer value")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(usage="print python3 {SCRIPT file_name} to start",
                                     description="A simple lying time-server, working with a client-script")
    offset = get_time_offset()
    start_server(offset)
