import logging
import subprocess
import sys


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Pacman():

    """Package manager setup"""

    @staticmethod
    def get_packages(current_dir: str):
        packages = ''
        with open(f'{current_dir}/_packages.ini', 'r') as file:
            for line in file:
                if not line.startswith('[') and not line.startswith('#') and line.strip() != '':
                    packages += f'{line.rstrip()} '
        return packages

    @staticmethod
    def install(pkgs: str):
        cmd = f'sudo pacman -S --needed --noconfirm {pkgs}'
        try:
            subprocess.run(cmd, shell=True, check=True)
            logger.info('Install packages')
        except Exception as err:
            logger.error(f'Install {err}')
            sys.exit(1)

    @staticmethod
    def explicit_keyring():
        cmd = 'sudo pacman -D --asexplicit archlinux-keyring',
        try:
            subprocess.run(cmd, shell=True, check=True)
            logger.info('Explicit Keyring')
        except Exception as err:
            logger.error(f'Explicit Keyring {err}')
            sys.exit(1)
