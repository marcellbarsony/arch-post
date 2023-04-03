import logging
import subprocess
import sys


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Pacman():

    """Package manager setup"""

    def dependencies(self):
        dependency='dmidecode'
        cmd = f'sudo pacman -S {dependency} --noconfirm'
        try:
            logger.info('Installing dependencies')
            subprocess.run(cmd, shell=True, check=True, stdout=subprocess.DEVNULL)
            logger.info('Installed dependencies')
        except KeyboardInterrupt as err:
            logger.warning('KeyboardInterrupt')
            sys.exit(0)
        except subprocess.CalledProcessError as err:
            logger.error('Installing dependencies')
            print(repr(err))
            sys.exit(1)
