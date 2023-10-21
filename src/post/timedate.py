import subprocess
import sys
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class SysTime():

    """
    Set system time & timezone
    https://wiki.archlinux.org/title/System_time
    https://wiki.archlinux.org/title/Network_Time_Protocol_daemon#
    """

    @staticmethod
    def time():
        cmd = "sudo timedatectl set-ntp true --no-ask-password"
        try:
            subprocess.run(cmd, shell=True, check=True, stdout=subprocess.DEVNULL)
            logger.info("Time & Date: System clock")
        except subprocess.CalledProcessError as err:
            logger.error("Time & Date: System clock")
            print(repr(err))
            sys.exit(1)

    @staticmethod
    def timezone(timezone: str):
        cmd = f"sudo timedatectl set-timezone {timezone}"
        try:
            subprocess.run(cmd, shell=True, check=True, stdout=subprocess.DEVNULL)
            logger.info("Time & Date: Timezone")
        except subprocess.CalledProcessError as err:
            logger.error("Time & Date: Timezone")
            print(repr(err))
            sys.exit(1)
