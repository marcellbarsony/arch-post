import os
import subprocess
import sys


class Helper():

    """AUR helper setup"""

    @staticmethod
    def directory(user, aur_helper):
        aur_dir = f'/home/{user}/.local/src/{aur_helper}/'
        os.makedirs(aur_dir, exist_ok=True)
        return aur_dir

    @staticmethod
    def clone(aur_helper, aur_dir):
        cmd = f'git clone https://aur.archlinux.org/{aur_helper}.git {aur_dir}'
        try:
            subprocess.run(cmd, shell=True, check=True, stdout=subprocess.DEVNULL)
            print('[+] AUR clone')
            return aur_dir
        except subprocess.CalledProcessError as err:
            if err.returncode == 128:
                print('[+] AUR clone: directory already exists')
                return aur_dir
            else:
                print('[-]', repr(err))
                sys.exit(1)

    @staticmethod
    def makepkg(aur_dir):
        os.chdir(aur_dir)
        cmd = f'makepkg -si --noconfirm'
        try:
            subprocess.run(cmd, shell=True, check=True, stdout=subprocess.DEVNULL)
            print('[+] AUR makepkg')
        except subprocess.CalledProcessError as err:
            print('[-]', repr(err))
            sys.exit(1)
