import subprocess
import sys
from .logger import *
from .s05_bitwarden import Bitwarden


class SecureShell():

    """SSH setup"""

    def __init__(self):
        self.logger = LogHelper()

    def kill(self):
        cmd = 'sudo pkill -9 -f ssh'
        try:
            subprocess.run(cmd, shell=True, check=True)
            self.logger.info('SSH: Kill')
        except Exception as err:
            self.logger.error('SSH: Kill')
            print(err)
            sys.exit(1)

    def start(self):
        cmd = 'eval "$(ssh-agent -s)"'
        try:
            subprocess.run(cmd, shell=True, check=True)
            self.logger.info('SSH: Launch')
        except Exception as err:
            self.logger.error('SSH: Launch')
            print(err)
            sys.exit(1)

    def keygen(self, user: str, ssh_key: str, gh_mail: str):
        gh_mail = Bitwarden().rbw_get('github', gh_mail)
        dir = f'/home/{user}/.ssh/id_ed25519'
        cmd = f'ssh-keygen -t ed25519 -N {ssh_key} -C {gh_mail} -f {dir}'
        try:
            subprocess.run(cmd, shell=True, check=True)
            self.logger.info('SSH: Keygen')
        except Exception as err:
            self.logger.error('SSH: Keygen')
            print(err)
            sys.exit(1)

    def add(self, user: str):
        cmd = f'ssh-add /home/{user}/.ssh/id_ed25519'
        try:
            subprocess.run(cmd, shell=True, check=True)
            self.logger.info('SSH: Add key')
        except Exception as err:
            self.logger.error('SSH: Add key')
            print('[-] SSH add', err)
            sys.exit(1)
