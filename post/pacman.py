import logging
import subprocess
import sys
import os


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Pacman():

    """Package manager setup"""

    @staticmethod
    def dependencies():
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

    @staticmethod
    def install():
        src_dir = os.path.abspath('pkgtest') # TODO: change dir to cfg
        for file in os.listdir(src_dir):
            file_path = os.path.join(src_dir, file)
            if os.path.isfile(file_path):
                cmd = f'sudo pacman -S --needed --noconfirm - < {file_path}'
                try:
                    subprocess.run(cmd, shell=True, check=True, text=True)
                    logger.info('Pacman: Install')
                except Exception as err:
                    logger.error(f'Pacman: Install {err}')
                    sys.exit(1)

    @staticmethod
    def install_package(package):
        cmd = f'sudo pacman -S --needed --noconfirm {package}'
        try:
            subprocess.run(cmd, shell=True, check=True)
            logger.info(f'[+] Installed {package}')
        except Exception as err:
            logger.error(f'[-] {err}')
            sys.exit(1)
