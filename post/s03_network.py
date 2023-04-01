import socket
import subprocess
import sys
from .logger import *


class WiFi():

    """WiFi settings"""

    def __init__(self):
        self.logger = LogHelper()

    def toggle(self, status: str) -> None:
        cmd = f'sudo nmcli radio wifi {status}'
        try:
            subprocess.run(cmd, shell=True, check=True)
            self.logger.info(f'WiFi: Toggle <{status}>')
        except subprocess.CalledProcessError as err:
            self.logger.error(f'WiFi: Toggle <{status}>')
            print(repr(err))
            sys.exit(1)

    def connect(self, ssid, password):
        cmd = f'nmcli device wifi connect {ssid} password {password}'
        try:
            subprocess.run(cmd, shell=True, check=True)
            self.logger.info(f'WiFi: Connect <{ssid}>')
        except subprocess.CalledProcessError as err:
            self.logger.error(f'WiFi: Connect <{ssid}>')
            print(repr(err))
            pass

class Network():

    """Network settings"""

    def __init__(self):
        self.logger = LogHelper()

    def check(self, ip: str, port: str) -> bool:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(5)
            s.connect((ip, int(port)))
            self.logger.info(f'Network: Connected')
            return True
        except socket.error:
            self.logger.warning(f'Network: Disconnected')
            print(socket.error)
            return False
