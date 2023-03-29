import subprocess
import sys
from .s05_bitwarden import Bitwarden


class SecureShell():

    """SSH setup"""

    @staticmethod
    def kill():
        cmd = 'sudo pkill -9 -f ssh'
        try:
            subprocess.run(cmd, shell=True, check=True)
            print('[+] SSH kill')
        except Exception as err:
            print('[-] SSH kill', err)
            sys.exit(1)

    @staticmethod
    def start():
        cmd = 'eval "$(ssh-agent -s)"'
        try:
            subprocess.run(cmd, shell=True, check=True)
            print('[+] SSH start')
        except Exception as err:
            print('[-] SSH start', err)
            sys.exit(1)

    @staticmethod
    def keygen(user, ssh_key, gh_mail):
        gh_mail = Bitwarden.rbw_get('github', gh_mail)
        dir = f'/home/{user}/.ssh/id_ed25519'
        cmd = f'ssh-keygen -t ed25519 -N {ssh_key} -C {gh_mail} -f {dir}'
        try:
            subprocess.run(cmd, shell=True, check=True)
            print('[+] SSH keygen')
        except Exception as err:
            print('[-] SSH keygen', err)
            sys.exit(1)

    @staticmethod
    def add(user):
        cmd = f'ssh-add /home/{user}/.ssh/id_ed25519'
        try:
            subprocess.run(cmd, shell=True, check=True)
            print('[+] SSH add')
        except Exception as err:
            print('[-] SSH add', err)
            sys.exit(1)
