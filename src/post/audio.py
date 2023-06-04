import logging
import sys
import subprocess


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Pipewire():

    """
    Docstring for Pipewire
    https://wiki.archlinux.org/title/Pipewire
    """

    @staticmethod
    def service():
        services = ['pipewire',
                    'pipewire-pulse',
                    'wireplumber']
        for service in services:
            cmd = f'systemctl --user enable {service}'
            try:
                subprocess.run(cmd, shell=True, check=True)
                logger.info(f'Enable <{service}>')
            except subprocess.CalledProcessError as err:
                logger.error(f'Enable <{service}> {err}')
                sys.exit(1)
