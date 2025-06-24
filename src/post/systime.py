import logging
import subprocess
import sys


"""
System Time (NTP) & Timezone
https://wiki.archlinux.org/title/System_time
https://wiki.archlinux.org/title/Network_Time_Protocol_daemon#
"""

def ntp():
    cmd = ["sudo", "timedatectl", "set-ntp", "true", "--no-ask-password"]
    try:
        subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL)
    except subprocess.CalledProcessError as err:
        logging.error("%s\n%s", cmd, repr(err))
        sys.exit(1)
    else:
        logging.info(cmd)

def time_zone(zone: str):
    cmd = ["timedatectl", "set-timezone", zone]
    try:
        subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL)
    except subprocess.CalledProcessError as err:
        logging.error("%s\n%s", cmd, repr(err))
        sys.exit(1)
    else:
        logging.info(cmd)
