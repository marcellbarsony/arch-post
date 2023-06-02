import logging
import os
import sys
import subprocess


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Wayland():

    """
    Docstring for Wayland
    https://wiki.archlinux.org/title/Wayland
    """

    @staticmethod
    def dm_install(aurhelper: str):
        cmd = f'{aurhelper} -S --noconfirm ly' # lemurs-git
        try:
            os.system('clear')
            subprocess.run(cmd, shell=True, check=True)
            logger.info('Display manager install')
        except subprocess.CalledProcessError as err:
            logger.error(f'Display manager install {err}')
            sys.exit(1)

    @staticmethod
    def dm_service():
        cmd = 'sudo systemctl enable ly.service' # lemurs.service
        try:
            subprocess.run(cmd, shell=True, check=True, stdout=subprocess.DEVNULL)
            logger.info('Display manager service')
        except subprocess.CalledProcessError as err:
            logger.error(f'Display manager service {err}')
            sys.exit(1)
