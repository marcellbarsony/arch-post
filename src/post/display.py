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
        os.system("clear")
        try:
            subprocess.run(cmd, shell=True, check=True)
            logging.info(cmd)
        except subprocess.CalledProcessError as err:
            logging.error(f"{cmd}: {err}")
            sys.exit(1)

    def service(self):
        cmd = f"sudo systemctl enable {self.loginman}.service"
        try:
            subprocess.run(cmd, shell=True, check=True, stdout=subprocess.DEVNULL)
            logging.info(cmd)
        except subprocess.CalledProcessError as err:
            logging.error(f"{cmd}: {err}")
            sys.exit(1)
