import subprocess
import sys
from .logger import *


class Initialize():

    """Initialize Arch base installer"""

    def __init__(self):
        self.logger = LogHelper()

    def dmi_data(self):
        cmd = 'sudo dmidecode -s system-product-name'
        try:
            out = subprocess.run(cmd, shell=True, check=True, capture_output=True)
            if 'VirtualBox' in str(out.stdout):
                print('[+] DMI <VirtualBox>')
                return 'virtualbox'
            if 'VMware Virtual Platform' in str(out.stdout):
                print('[+] DMI <VMWare>')
                return 'vmware'
        except subprocess.CalledProcessError as err:
            print('[-]', repr(err))
            sys.exit(1)

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
    def sys_clock():
        cmd = 'sudo timedatectl set-ntp true --no-ask-password'
        try:
            subprocess.run(cmd, shell=True, check=True, stdout=subprocess.DEVNULL)
            print('[+] System clock')
        except subprocess.CalledProcessError as err:
            print('[-] System clock', {err})
            sys.exit(1)
