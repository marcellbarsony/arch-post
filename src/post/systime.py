import logging
import subprocess
import sys


"""
Set System Time (NTP) & Timezone
https://wiki.archlinux.org/title/System_time
https://wiki.archlinux.org/title/Network_Time_Protocol_daemon#
"""

def ntp():
    cmd = "sudo timedatectl set-ntp true --no-ask-password"
    try:
        subprocess.run(cmd, shell=True, check=True, stdout=subprocess.DEVNULL)
        print(":: [+] SYSTIME :: ", cmd)
        logging.info(cmd)
    except subprocess.CalledProcessError as err:
        print(":: [-] SYSTIME :: ", repr(err))
        logging.error(f"{cmd}: {repr(err)}")
        sys.exit(1)

def time_zone(zone: str):
    cmd = f"timedatectl set-timezone {zone}"
    try:
        subprocess.run(cmd, shell=True, check=True, stdout=subprocess.DEVNULL)
        print(":: [+] SYSTIME :: ", cmd)
        logging.info(cmd)
    except subprocess.CalledProcessError as err:
        print(":: [-] SYSTIME :: ", err)
        logging.error(f"{cmd}\n{err}")
        sys.exit(1)
