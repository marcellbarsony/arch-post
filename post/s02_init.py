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
                self.logger.info('DMI data: <VirtualBox>')
                return 'virtualbox'
            if 'VMware Virtual Platform' in str(out.stdout):
                self.logger.info('DMI data: <VMWare>')
                return 'vmware'
        except subprocess.CalledProcessError as err:
            self.logger.error('DMI: Cannot fetch DMI information')
            print(repr(err))
            sys.exit(1)

    def timezone(self, timezone: str):
        cmd = f'sudo timedatectl set-timezone {timezone}'
        try:
            subprocess.run(cmd, shell=True, check=True)
            self.logger.info('Time & Date: Timezone')
        except subprocess.CalledProcessError as err:
            self.logger.error('Time & Date: Timezone')
            print(repr(err))
            sys.exit(1)

    def sys_clock(self):
        cmd = 'sudo timedatectl set-ntp true --no-ask-password'
        try:
            subprocess.run(cmd, shell=True, check=True, stdout=subprocess.DEVNULL)
            self.logger.info('Time & Date: System clock')
        except subprocess.CalledProcessError as err:
            self.logger.error('Time & Date: System clock')
            print({err})
            sys.exit(1)
