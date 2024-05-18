import logging
import subprocess
import sys


"""
Package manager setup
https://wiki.archlinux.org/title/Pacman/Package_signing
"""

def explicit_keyring():
    cmd = "sudo pacman -D --asexplicit archlinux-keyring"
    try:
        subprocess.run(cmd, shell=True, check=True, stdout=subprocess.DEVNULL)
        print(":: [+] PACMAN :: Keyring")
        logging.info(cmd)
    except subprocess.CalledProcessError as err:
        print(":: [-] PACMAN :: Keyring :: ", err)
        logging.error(f"{cmd}: {repr(err)}")
        sys.exit(1)

def update():
    cmd = "sudo pacman -Sy --noconfirm"
    try:
        subprocess.run(cmd, shell=True, check=True, stdout=subprocess.DEVNULL)
        print(":: [+] PACMAN :: Update")
        logging.info(cmd)
    except subprocess.CalledProcessError as err:
        print(":: [-] PACMAN :: Update :: ", err)
        logging.error(f"{cmd}\n{repr(err)}")
        sys.exit(1)
