import logging
import subprocess
import sys


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Systemd():

    """
    Docstring for managing services
    https://wiki.archlinux.org/title/Systemd
    """

    @staticmethod
    def enable():
        # spotifyd
        pass

    @staticmethod
    def enable_user():
        services = ['pipewire', 'pipewire-pulse', 'wireplumber']
        for service in services:
            cmd = f'systemctl --user enable {service}'
            try:
                subprocess.run(cmd, shell=True, check=True)
                logger.info(f'Service: Enable <{service}>')
            except Exception as err:
                logger.error(f'Service: Enable <{service}> {err}')
                sys.exit(1)
