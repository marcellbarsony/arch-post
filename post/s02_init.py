import subprocess
import sys


class Initialize():

    """Initialize Arch base installer"""

    @staticmethod
    def timezone(timezone):
        cmd = f'sudo timedatectl set-timezone {timezone}'
        try:
            subprocess.run(cmd, shell=True, check=True)
            print('[+] Timedatectl set-timezone')
        except subprocess.CalledProcessError as err:
            print('[-]', repr(err))
            sys.exit(1)

    @staticmethod
    def install(dependencies):
        for dependency in dependencies:
            cmd = f'sudo pacman -S {dependency} --noconfirm'
            try:
                subprocess.run(cmd, shell=True, check=True)
                print('[+] Dependencies')
            except subprocess.CalledProcessError as err:
                print('[-]', repr(err))
                sys.exit(1)
