import subprocess
import sys
from .logger import *
from .s05_bitwarden import *

class GitHub():

    """GitHub setup"""

    def __init__(self):
        self.logger = LogHelper()

    def auth_login(self, gh_token: str):
        cmd = 'gh auth login --with-token'
        token = Bitwarden().rbw_get('github', gh_token)
        try:
            subprocess.run(cmd, shell=True, check=True, input=token)
            self.logger.info('GitHub: Auth login')
        except subprocess.CalledProcessError as err:
            self.logger.error(f'GitHub: Auth login {err}')
            sys.exit(1)

    def auth_status(self):
        cmd = 'gh auth status'
        try:
            subprocess.run(cmd, shell=True, check=True)
            self.logger.info('GitHub: Auth status')
        except subprocess.CalledProcessError as err:
            self.logger.error('GitHub: Auth status')
            print(err)
            sys.exit(1)

    def add_pubkey(self, user: str, gh_pubkey: str):
        cmd = f'gh ssh-key add /home/{user}/.ssh/id_ed25519.pub -t ${gh_pubkey}'
        try:
            subprocess.run(cmd, shell=True, check=True)
            self.logger.info('GitHub: Add public key')
        except subprocess.CalledProcessError as err:
            self.logger.error(f'GitHub: Add public key {err}')
            sys.exit(1)

    def test(self):
        cmd = 'ssh -T git@github.com'
        try:
            res = subprocess.run(cmd, shell=True, check=True)
            if res.returncode in [0, 1]:
                cmd = 'ssh-keyscan github.com >> ~/.ssh/known_hosts'
                try:
                    subprocess.run(cmd, shell=True, check=True)
                    self.logger.info('GitHub: SSH test')
                except subprocess.CalledProcessError as err:
                    self.logger.error(f'GitHub: SSH test {err}')
                    sys.exit(1)
        except subprocess.CalledProcessError as err:
            self.logger.error(f'GitHub: SSH test {err}')
            sys.exit(1)

    @staticmethod
    def known_hosts():
        print('[TODO] known hosts')
        # TODO: gh_known_hosts
        # ssh-keyscan github.com >> ~/.ssh/known_hosts
        pass
