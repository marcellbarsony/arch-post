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
    except subprocess.CalledProcessError as err:
        logging.error(f"{cmd}: {repr(err)}")
        print(":: [-] PACMAN :: Keyring :: ", err)
        sys.exit(1)
    else:
        logging.info(cmd)
        print(":: [+] PACMAN :: Keyring")

def update():
    cmd = "sudo pacman -Sy --noconfirm"
    try:
        subprocess.run(cmd, shell=True, check=True, stdout=subprocess.DEVNULL)
    except subprocess.CalledProcessError as err:
        logging.error(f"{cmd}\n{repr(err)}")
        print(":: [-] PACMAN :: Update :: ", err)
        sys.exit(1)
    else:
        logging.info(cmd)
        print(":: [+] PACMAN :: Update")

def remove_orphans():
    """https://wiki.archlinux.org/title/Pacman/Tips_and_tricks#Removing_unused_packages_(orphans)"""
    cmd = "sudo pacman -Qtdq | pacman -Rns -"
    try:
        subprocess.run(cmd, shell=True, check=True)
    except subprocess.CalledProcessError as err:
        logging.error(err)
        print(":: [-] PACMAN :: Remove orphans :: ", err)
    else:
        logging.info(cmd)
        print(":: [+] PACMAN :: Remove orphans")
