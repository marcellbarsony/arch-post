import sys
import subprocess


class Install():

    """Docstring for Base"""

    @staticmethod
    def install(packages):
        cmd = f'{packages} | sudo pacman -S --needed --noconfirm -'
        try:
            subprocess.run(cmd, shell=True, check=True)
            print('[+] PACMAN install')
        except Exception as err:
            print('[-] PACMAN install', err)
            sys.exit(1)
