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
    except subprocess.CalledProcessError as err:
        logging.error(f"{cmd}: {repr(err)}")
        print(":: [-] SYSTIME :: ", repr(err))
        sys.exit(1)
    else:
        logging.info(cmd)
        print(":: [+] SYSTIME :: ", cmd)

def time_zone(zone: str):
    cmd = f"timedatectl set-timezone {zone}"
    try:
        subprocess.run(cmd, shell=True, check=True, stdout=subprocess.DEVNULL)
    except subprocess.CalledProcessError as err:
        logging.error(f"{cmd}\n{err}")
        print(":: [-] SYSTIME :: ", err)
        sys.exit(1)
    else:
        logging.info(cmd)
        print(":: [+] SYSTIME :: ", cmd)
