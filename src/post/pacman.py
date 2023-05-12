import logging
import shutil
import subprocess
import sys


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Pacman():

    """Package manager setup"""

    @staticmethod
    def explicit_keyring():
        cmd = 'sudo pacman -D --asexplicit archlinux-keyring',
        try:
            subprocess.run(cmd, shell=True, check=True)
            logger.info('Explicit Keyring')
        except Exception as err:
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
        dst = '/etc/pacman.d/mirrorlist.bak'
        shutil.copy2(self.mirrorlist, dst)

    def update(self):
        cmd = f'reflector --latest 20 --protocol https --connection-timeout 5 --sort rate --save {self.mirrorlist}'
        try:
            print('REFLECTOR: Updating Pacman mirrorlist...')
            subprocess.run(cmd, shell=True, check=True, stdout=subprocess.DEVNULL)
            print(f'[+] REFLECTOR: Mirrorlist update')
        except subprocess.CalledProcessError as err:
            print(f'[-] REFLECTOR: Mirorlist update', err)
            sys.exit(1)
