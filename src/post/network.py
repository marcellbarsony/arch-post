# import logging
import socket
import subprocess
import sys


"""WiFi settings"""

def toggle(status: str) -> None:
    cmd = f"sudo nmcli radio wifi {status}"
    try:
        subprocess.run(cmd, shell=True, check=True)
        # logger.info(f"Wi-Fi status: {status}")
    except subprocess.CalledProcessError as err:
        print(repr(err))
        sys.exit(1)

def connect(ssid, password):
    cmd = f"nmcli device wifi connect {ssid} password {password}"
    try:
        subprocess.run(cmd, shell=True, check=True)
        # logger.info(f"Wi-Fi connected {ssid}")
    except subprocess.CalledProcessError as err:
        print(repr(err))
        pass


"""Network settings"""

def check(ip: str, port: str) -> bool:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5)
        s.connect((ip, int(port)))
        # logger.info("Network: Connected")
        return True
    except socket.error:
        # logger.info("Network: Disconnected")
        print(socket.error)
        return False
