import logging
import os
import sys
import subprocess


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class DisplayManager():

    """
    Docstring for Display manager
    """

    def __init__(self, loginman: str):
        self.loginman = loginman

    def install(self, aurhelper: str):
        cmd = f'{aurhelper} -S --noconfirm {self.loginman}'
        try:
            os.system('clear')
            subprocess.run(cmd, shell=True, check=True)
            logger.info('Display manager install')
        except subprocess.CalledProcessError as err:
            logger.error(f'Display manager install {err}')
            sys.exit(1)

    def service(self):
        cmd = f'sudo systemctl enable {self.loginman}.service'
        try:
            subprocess.run(cmd, shell=True, check=True, stdout=subprocess.DEVNULL)
            logger.info('Display manager service')
        except subprocess.CalledProcessError as err:
            logger.error(f'Display manager service {err}')
            sys.exit(1)
