import logging
import subprocess
import sys
from .bitwarden import *


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class GitSetup():

    """Git setup w/GitHub"""

    @staticmethod
    def authLogin(gh_token: str):
        cmd = 'gh auth login --with-token'
        token = Bitwarden().rbwGet('github', gh_token)
        try:
            subprocess.run(cmd, shell=True, check=True, input=token.encode())
            logger.info('Auth login')
        except subprocess.CalledProcessError as err:
            logger.error(f'Auth login', err)
            sys.exit(1)

    @staticmethod
    def authStatus():
        cmd = 'gh auth status'
        try:
            subprocess.run(cmd, shell=True, check=True)
            logger.info('Auth status')
        except subprocess.CalledProcessError as err:
            print(err)
            sys.exit(1)

    @staticmethod
    def addPubkey(user: str, gh_pubkey: str):
        cmd = f'gh ssh-key add /home/{user}/.ssh/id_ed25519.pub -t {gh_pubkey}'
        try:
            subprocess.run(cmd, shell=True, check=True)
            logger.info('Add public key')
        except subprocess.CalledProcessError as err:
            logger.error('Add public key', err)
            sys.exit(1)

    @staticmethod
    def knownHosts():
        cmd = 'ssh-keyscan github.com >> ~/.ssh/known_hosts'
        try:
            subprocess.run(cmd, shell=True, check=True)
            logger.info('Known hosts')
        except subprocess.CalledProcessError as err:
            logger.error('Known hosts', err)
            sys.exit(1)

    @staticmethod
    def test():
        cmd = 'ssh -T git@github.com'
        res = subprocess.run(cmd, shell=True)
        if res.returncode in [0, 1]:
            logger.info('SSH test')
        else:
            logger.error('SSH test')
            sys.exit(res.returncode)

    @staticmethod
    def config(gh_user: str, gh_mail: str):
        user_name = Bitwarden().rbwGet('github', gh_user)
        user_mail = Bitwarden().rbwGet('github', gh_mail)
        cmd_list = [f'git config --global user.name "{user_name}"',
                    f'git config --global user.email "{user_mail}"',
                    f'git config --global init.defaultBranch main']
        for cmd in cmd_list:
            try:
                subprocess.run(cmd, shell=True, check=True)
                logger.info('Git config')
            except subprocess.CalledProcessError as err:
                logger.error('Git config', err)
                sys.exit(1)
