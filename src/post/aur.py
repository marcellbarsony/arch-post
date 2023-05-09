import logging
import os
import subprocess
import sys


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class AURhelper():

    """AUR helper setup"""

    def __init__(self, user: str, aur_helper: str):
        self.user = user
        self.aur_helper = aur_helper
        self.aur_dir = f'/home/{self.user}/.local/src/{self.aur_helper}/'

    def make_dir(self):
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
                sys.exit(1)

    def make_pkg(self):
        current_dir = os.getcwd()
        cmd = f'makepkg -si --noconfirm'
        try:
            os.chdir(self.aur_dir)
            subprocess.run(cmd, shell=True, check=True, stdout=subprocess.DEVNULL)
            os.chdir(current_dir)
            logger.info('AUR: Makepkg')
        except subprocess.CalledProcessError as err:
            os.chdir(current_dir)
            logger.error('AUR: Makepkg')
            print(repr(err))
            sys.exit(1)

    @staticmethod
    def install(current_dir: str, aurhelper: str, sudo: str):
        packages = ''
        with open(f'{current_dir}/src/pkg/pkg_aur.ini', 'r') as file:
            for line in file:
                if not line.startswith('[') and not line.startswith('#') and line.strip() != '':
                    packages += f'{line.rstrip()} '
        cmd = f'sudo {aurhelper} -S --noconfirm {packages}'
        try:
            subprocess.run(cmd, shell=True, input=sudo, check=True, text=True)
            logger.info('AUR install')
        except Exception as err:
            logger.error(f'AUR install {err}')
            sys.exit(1)
