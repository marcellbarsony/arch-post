import logging
import sys
import subprocess


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Install():

    """Docstring for Pacman install"""

    def install(self, packages):
        cmd = f'{packages} | sudo pacman -S --needed --noconfirm -'
        try:
            subprocess.run(cmd, shell=True, check=True)
            logger.info('Pacman: Install')
        except Exception as err:
            logger.error(f'Pacman: Install {err}')
            sys.exit(1)
