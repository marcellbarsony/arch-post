import subprocess
import sys


class SecureShell():

    """SSH setup"""

    @staticmethod
    def kill():
        cmd = 'sudo pkill -9 -f ssh'
        try:
            out = subprocess.run(cmd, shell=True)
            print('[+] SSH kill', out)
        except Exception as err:
            print('[-] SSH kill', err)
            sys.exit(1)

    @staticmethod
    def start():
        cmd = 'eval "$(ssh-agent -s)"'
        try:
            out = subprocess.run(cmd, shell=True)
            print('[+] SSH start', out)
        except Exception as err:
            print('[-] SSH start', err)
            sys.exit(1)

    @staticmethod
    def keygen(user, ssh_key, gh_mail, dir):
        dir = f'/home/{user}/.ssh/id_ed25519'
        cmd = f'ssh-keygen -t ed25519 -N {ssh_key} -C {gh_mail} -f {dir}'
        try:
            out = subprocess.run(cmd, shell=True)
            print('[+] SSH keygen', out)
        except Exception as err:
            print('[-] SSH keygen', err)
            sys.exit(1)

