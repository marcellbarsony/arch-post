import logging
import subprocess
import sys


class TimeDate():

    """
    Set System time & Timezone
    https://wiki.archlinux.org/title/System_time
    https://wiki.archlinux.org/title/Network_Time_Protocol_daemon#
    """

    @staticmethod
    def time():
        cmd = "sudo timedatectl set-ntp true --no-ask-password"
        try:
            subprocess.run(cmd, shell=True, check=True, stdout=subprocess.DEVNULL)
            logging.info(f"Time & Date: NTP - {cmd}")
        except subprocess.CalledProcessError as err:
            logging.error(f"Time & Date: NTP - {cmd}: {repr(err)}")
            print(repr(err))
            sys.exit(1)

    @staticmethod
    def timezone(timezone: str):
        cmd = f"sudo timedatectl set-timezone {timezone}"
        try:
            subprocess.run(cmd, shell=True, check=True, stdout=subprocess.DEVNULL)
            logging.info(f"Time & Date: Timezone - {cmd}")
        except subprocess.CalledProcessError as err:
            logging.error(f"Time & Date: Timezone - {cmd}: {repr(err)}")
            print(repr(err))
            sys.exit(1)
