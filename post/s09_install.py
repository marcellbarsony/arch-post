import sys
import subprocess
from .logger import *


class Install():

    """Docstring for Pacman install"""

    def __init__(self):
        self.logger = LogHelper()

    def install(self, packages):
        cmd = f'{packages} | sudo pacman -S --needed --noconfirm -'
        try:
            subprocess.run(cmd, shell=True, check=True)
            self.logger.info('Pacman: Install')
        except Exception as err:
            self.logger.error(f'Pacman: Install {err}')
            sys.exit(1)
