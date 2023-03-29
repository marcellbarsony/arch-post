
import subprocess
import sys


class Pacman():

    """Package manager setup"""

    @staticmethod
    def dependencies():
        dependency='dmidecode'
        cmd = f'sudo pacman -S {dependency} --noconfirm'
        try:
            subprocess.run(cmd, shell=True, check=True, stdout=subprocess.DEVNULL)
            print('[+] Dependencies')
        except subprocess.CalledProcessError as err:
            print('[-]', repr(err))
            sys.exit(1)
