import os
import subprocess
import sys


class Aur():

    """Arch User Repository setup"""

    @staticmethod
    def clone(user, aur_helper):
        dir = f'/home/{user}/.local/src/{aur_helper}/'
        os.makedirs(dir, exist_ok=True)
        try:
            cmd = f'git clone https://aur.archlinux.org/{aur_helper}.git {dir}'
            subprocess.run(cmd, shell=True, check=True)
            print('[+] AUR clone')
            return dir
        except subprocess.CalledProcessError as err:
            if err.returncode == 128:
                print('[+] AUR clone: directory already exists')
                return dir
            else:
                print(repr(err))
                sys.exit(1)

    @staticmethod
    def makepkg(dir):
        os.chdir(dir)
        cmd = f'makepkg -si --noconfirm'
        try:
            subprocess.run(cmd, shell=True, check=True)
            print('[+] AUR makepkg')
        except subprocess.CalledProcessError as err:
            print('[-]', repr(err))
            sys.exit(1)
