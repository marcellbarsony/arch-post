import logging
import sys
import subprocess


"""
Docstring for Pipewire
https://wiki.archlinux.org/title/Pipewire
"""

def service():
    services = [
        "pipewire",
        "wireplumber"
    ]
    for service in services:
        cmd = f"systemctl --user enable {service}"
        try:
            subprocess.run(cmd, shell=True, check=True)
        except subprocess.CalledProcessError as err:
            logging.error(f"{cmd}\n{err}")
            sys.exit(1)
        else:
            logging.info(cmd)
