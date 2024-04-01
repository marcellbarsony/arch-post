import logging
import os
import sys
import subprocess


def install(aurhelper: str, loginman: str):
    cmd = f"{aurhelper} -S --noconfirm {loginman}"
    os.system("clear")
    try:
        subprocess.run(cmd, shell=True, check=True)
        logging.info(cmd)
    except subprocess.CalledProcessError as err:
        logging.error(f"{cmd}: {err}")
        sys.exit(1)

def service(loginman: str):
    cmd = f"sudo systemctl enable {loginman}.service"
    try:
        subprocess.run(cmd, shell=True, check=True, stdout=subprocess.DEVNULL)
        logging.info(cmd)
    except subprocess.CalledProcessError as err:
        logging.error(f"{cmd}: {err}")
        sys.exit(1)
