import logging
import os
import subprocess
import sys


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class AurHelper():

    """AUR helper setup"""

    def __init__(self, user, aur_helper):
        self.user = user
        self.aur_helper = aur_helper
        self.aur_dir = f'/home/{self.user}/.local/src/{self.aur_helper}/'

    def makedir(self):
        os.makedirs(self.aur_dir, exist_ok=True)

    def clone(self):
        cmd = f'git clone https://aur.archlinux.org/{self.aur_helper}.git {self.aur_dir}'
        try:
            subprocess.run(cmd, shell=True, check=True, stdout=subprocess.DEVNULL)
            logger.info('AUR: Clone')
        except subprocess.CalledProcessError as err:
            if err.returncode == 128:
                logger.warning('AUR directory already exists')
                pass
            else:
                logger.error('AUR: Clone')
                print(repr(err))

    def makepkg(self):
        os.chdir(self.aur_dir)
        cmd = f'makepkg -si --noconfirm'
        try:
            subprocess.run(cmd, shell=True, check=True, stdout=subprocess.DEVNULL)
            logger.info('AUR: Makepkg')
        except subprocess.CalledProcessError as err:
            logger.error('AUR: Makepkg')
            print(repr(err))
            sys.exit(1)
