import logging
import shutil
import subprocess
import sys


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Pacman():

    """
    Package manager setup
    https://wiki.archlinux.org/title/Pacman/Package_signing
    """

    @staticmethod
    def keyring():
        cmd = 'sudo pacman -D --asexplicit archlinux-keyring',
        try:
            subprocess.run(cmd, shell=True, check=True, stdout=subprocess.DEVNULL)
            logger.info('Explicit Keyring')
        except subprocess.CalledProcessError as err:
            logger.error(f'Explicit Keyring {err}')
            sys.exit(1)


class Mirrorlist():

    """
    Update & back-up mirrolist
    https://wiki.archlinux.org/title/Reflector
    """

    def __init__(self):
        self.mirrorlist = '/etc/pacman.d/mirrorlist'

    def backup(self):
        src = '/etc/pacman.d/mirrorlist'
        dst = '/etc/pacman.d/mirrorlist.bak'
        cmd = f'sudo cp -r {src} {dst}'
        try:
            subprocess.run(cmd, shell=True, check=True)
            logger.info('Mirrorlist backup')
        except subprocess.CalledProcessError as err:
            logger.error(f'Mirrorlist backup {err}')
            sys.exit(1)

    def update(self):
        cmd = f'sudo reflector --latest 20 --protocol https --connection-timeout 5 --sort rate --save {self.mirrorlist}'
        try:
            logger.info('Updating mirrorlist...')
            subprocess.run(cmd, shell=True, check=True, stdout=subprocess.DEVNULL)
            logger.info('Mirrorlist update')
        except subprocess.CalledProcessError as err:
            logger.error(f'Mirrorlist update {err}')
            sys.exit(1)
