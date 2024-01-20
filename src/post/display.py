import logging
import os
import sys
import subprocess


class DisplayManager():

    """
    Docstring for Display manager
    Wayland setup
    """

    def __init__(self, loginman: str):
        self.loginman = loginman

    def install(self, aurhelper: str):
        cmd = f"{aurhelper} -S --noconfirm {self.loginman}"
        try:
            os.system("clear")
            subprocess.run(cmd, shell=True, check=True)
            logging.info(f"Display manager: Install - {cmd}")
        except subprocess.CalledProcessError as err:
            logging.error(f"Display manager: Install - {cmd}: {err}")
            sys.exit(1)

    def service(self):
        cmd = f"sudo systemctl enable {self.loginman}.service"
        try:
            subprocess.run(cmd, shell=True, check=True, stdout=subprocess.DEVNULL)
            logging.info(f"Display manager: Service - {cmd}")
        except subprocess.CalledProcessError as err:
            logging.error(f"Display manager: Service - {cmd}: {err}")
            sys.exit(1)
