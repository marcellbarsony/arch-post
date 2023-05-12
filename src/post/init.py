import getpass
import subprocess
import sys
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Initialize():

    """Initialize Arch post installer"""

    @staticmethod
    def get_sudo(user: str) -> str:
        while True:
            sudo = getpass.getpass(f'[sudo] password for {user}: ')
            cmd = f'echo {sudo} | sudo -S true'
            result = subprocess.run(cmd, shell=True, capture_output=True)
            if result.returncode == 0:
                return sudo
            else:
                logger.error(f'Incorrect sudo password for {user}')

    @staticmethod
    def sys_timezone(timezone: str):
        cmd = f'sudo timedatectl set-timezone {timezone}'
        try:
            subprocess.run(cmd, shell=True, check=True)
            logger.info('Time & Date: Timezone')
        except subprocess.CalledProcessError as err:
            logger.error('Time & Date: Timezone')
            print(repr(err))
            sys.exit(1)

    @staticmethod
    def sys_clock():
        cmd = 'sudo timedatectl set-ntp true --no-ask-password'
        try:
            subprocess.run(cmd, shell=True, check=True, stdout=subprocess.DEVNULL)
            logger.info('Time & Date: System clock')
        except subprocess.CalledProcessError as err:
            logger.error('Time & Date: System clock')
            print(repr(err))
            sys.exit(1)
