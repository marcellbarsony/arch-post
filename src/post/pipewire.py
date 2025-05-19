import logging
import sys
import subprocess


"""
Pipewire
https://wiki.archlinux.org/title/Pipewire
"""

def service():
    services = [
        "pipewire",
        "wireplumber"
    ]
    for service in services:
        cmd = ["systemctl", "--user", "enable", service]
        try:
            subprocess.run(cmd, check=True)
        except subprocess.CalledProcessError as err:
            logging.error(f"{cmd}\n{err}")
            print(f":: [-] :: SERVICE :: Enable {service} ::", err)
            sys.exit(1)
        else:
            logging.info(cmd)
