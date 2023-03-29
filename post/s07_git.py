import subprocess
import sys
from .s05_bitwarden import *

class GitHub():

    """GitHub setup"""

    @staticmethod
    def auth_login(gh_token):
        cmd = 'gh auth login --with-token'
        token = Bitwarden.rbw_get('github', gh_token)
        try:
            subprocess.run(cmd, shell=True, check=True, input=token)
            print('[+] GITHUB auth login')
        except subprocess.CalledProcessError as err:
            print('[-] GITHUB auth login', err)
            sys.exit(1)

    @staticmethod
    def auth_status():
        cmd = 'gh auth status'
        try:
            subprocess.run(cmd, shell=True, check=True)
            print('[+] GITHUB auth status')
        except subprocess.CalledProcessError as err:
            print('[-] GITHUB auth status', err)
            sys.exit(1)

    @staticmethod
    def add_pubkey(user, gh_pubkey):
        cmd = f'gh ssh-key add /home/{user}/.ssh/id_ed25519.pub -t ${gh_pubkey}'
        try:
            subprocess.run(cmd, shell=True, check=True)
            print('[+] GITHUB auth status')
        except subprocess.CalledProcessError as err:
            print('[-] GITHUB auth status', err)
            sys.exit(1)

    @staticmethod
    def test():
        cmd = 'ssh -T git@github.com'
        try:
            res = subprocess.run(cmd, shell=True, check=True)
            if res.returncode in [0, 1]:
                cmd = 'ssh-keyscan github.com >> ~/.ssh/known_hosts'
                try:
                    subprocess.run(cmd, shell=True, check=True)
                    print('[+] GITHUB SSH test')
                except subprocess.CalledProcessError as err:
                    print('[-] GITHUB SSH test', err)
                    sys.exit(1)
        except subprocess.CalledProcessError as err:
            print('[-] GITHUB SSH test', err)
            sys.exit(1)

    @staticmethod
    def known_hosts():
        print('[TODO] known hosts')
        # TODO: gh_known_hosts
        # ssh-keyscan github.com >> ~/.ssh/known_hosts
        pass
