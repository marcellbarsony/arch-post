import subprocess
import sys
from .logger import *


class Pacman():

    """Package manager setup"""

    def __init__(self):
        self.logger = LogHelper()

    def dependencies(self):
        dependency='dmidecode'
        cmd = f'sudo pacman -S {dependency} --noconfirm'
        try:
            self.logger.info('Installing dependencies')
            subprocess.run(cmd, shell=True, check=True, stdout=subprocess.DEVNULL)
            self.logger.info('Installed dependencies')
        except KeyboardInterrupt as err:
            self.logger.warning('KeyboardInterrupt')
            sys.exit(0)
        except subprocess.CalledProcessError as err:
            self.logger.error('Installing dependencies')
            print(repr(err))
            sys.exit(1)
