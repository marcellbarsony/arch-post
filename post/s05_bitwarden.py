import logging
import subprocess
import sys


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Bitwarden():

    """Bitwarden setup with rbw"""

    @staticmethod
    def install(aur_helper):
        cmd = f'{aur_helper} -S --noconfirm rbw'
        try:
            subprocess.run(cmd, shell=True, check=True)
            logger.info('Bitwarden: RBW install')
        except subprocess.CalledProcessError as err:
            logger.error(f'Bitwarden: RBW install {err}')
            sys.exit(1)

    @staticmethod
    def register(mail: str, url: str, timeout: str) -> bool:
        commands = [f'rbw config set email {mail}',
                    f'rbw config set base_url {url}',
                    f'rbw config set lock_timeout {timeout}',
                    'rbw register',
                    'rbw sync']
        success = True
        for cmd in commands:
            try:
                subprocess.run(cmd, shell=True, check=True)
                #self.logger.info('Bitwarden: RBW register')
            except subprocess.CalledProcessError as err:
                #self.logger.error('Bitwarden: RBW register')
                print(repr(err))
                success = False
                break
        return success

    def rbw_get(self, name: str, item: str) -> str:
        cmd = f'rbw get {name} --full | grep "{item}" | cut -d " " -f 2'
        out = subprocess.run(cmd, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='UTF-8')
        if "ERROR" in str(out.stderr):
            logger.error(f'Bitwarden: Fetch data <{name}> <{item}>')
            sys.exit(1)
        logger.info(f'Bitwarden: Fetch data')
        return out.stdout
