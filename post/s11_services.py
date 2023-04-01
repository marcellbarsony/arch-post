import subprocess
import sys
from .logger import *


class Services():

    """Docstring for Services"""

    def __init__(self):
        self.logger = LogHelper()

    def enable(self):
        services = ['spotifyd'] # ly
        for service in services:
            cmd = f'sudo systemctl enable {service}.service'
            try:
                subprocess.run(cmd, shell=True, check=True)
                self.logger.info(f'Service: Enable <{service}>')
            except Exception as err:
                self.logger.error(f'Service: Enable <{service}> {err}')
                sys.exit(1)
