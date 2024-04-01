import logging
import subprocess
import sys


"""
Set System Time & Timezone
https://wiki.archlinux.org/title/System_time
https://wiki.archlinux.org/title/Network_Time_Protocol_daemon#
"""

def ntp():
    cmd = "sudo timedatectl set-ntp true --no-ask-password"
    try:
        subprocess.run(cmd, shell=True, check=True, stdout=subprocess.DEVNULL)
        logging.info(cmd)
        print("[+] NTP")
    except subprocess.CalledProcessError as err:
        logging.error(f"{cmd}: {repr(err)}")
        print(repr(err))
        sys.exit(1)

def timezone(timezone: str):
    cmd = f"sudo timedatectl set-timezone {timezone}"
    try:
        subprocess.run(cmd, shell=True, check=True, stdout=subprocess.DEVNULL)
        print("[+] Timezone")
        logging.info(cmd)
    except subprocess.CalledProcessError as err:
        logging.error(f"{cmd} - {repr(err)}")
        print(repr(err))
        sys.exit(1)
