import os
import subprocess
import sys
from .logger import *


class Helper():

    """AUR helper setup"""

    def __init__(self):
        self.logger = LogHelper()

    def directory(self, user: str, aur_helper: str) -> str:
        aur_dir = f'/home/{user}/.local/src/{aur_helper}/'
        os.makedirs(aur_dir, exist_ok=True)
        return aur_dir

    def clone(self, aur_helper: str, aur_dir: str):
        cmd = f'git clone https://aur.archlinux.org/{aur_helper}.git {aur_dir}'
        try:
            subprocess.run(cmd, shell=True, check=True, stdout=subprocess.DEVNULL)
            self.logger.info('AUR: Clone')
        except subprocess.CalledProcessError as err:
            if err.returncode == 128:
                self.logger.warning('AUR directory already exists')
                pass
            else:
                self.logger.error('AUR: Clone')
                print(repr(err))

    def makepkg(self, aur_dir: str):
        os.chdir(aur_dir)
        cmd = f'makepkg -si --noconfirm'
        try:
            subprocess.run(cmd, shell=True, check=True, stdout=subprocess.DEVNULL)
            self.logger.info('AUR: Makepkg')
        except subprocess.CalledProcessError as err:
            self.logger.error('AUR: Makepkg')
            print(repr(err))
            sys.exit(1)
