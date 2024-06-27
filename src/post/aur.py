import logging
import os
import subprocess
import sys


"""AUR helper setup"""

def mkdir(aur_dir: str):
    os.makedirs(aur_dir, exist_ok=True)
    logging.info(aur_dir)
    print(":: [+] AUR :: Mkdir")

def clone(aur_dir: str, aur_helper: str):
    cmd = f"git clone https://aur.archlinux.org/{aur_helper}.git {aur_dir}"
    try:
        subprocess.run(cmd, shell=True, check=True, stdout=subprocess.DEVNULL)
        logging.info(cmd)
        print(":: [+] AUR :: Clone")
    except subprocess.CalledProcessError as err:
        if err.returncode == 128:
            logging.info(f"Directory already exists: {aur_dir}")
        else:
            logging.error(f"{cmd}\n{repr(err)}")
            sys.exit(1)

def mkpkg(aur_dir: str):
    current_dir = os.getcwd()
    cmd = f"makepkg -rsi --noconfirm"
    try:
        os.chdir(aur_dir)
        subprocess.run(cmd, shell=True, check=True, stdout=subprocess.DEVNULL)
        logging.info(cmd)
        os.chdir(current_dir)
        os.system("clear")
    except subprocess.CalledProcessError as err:
        logging.error(f"{cmd}\n{repr(err)}")
        print(":: [-] AUR :: Makepkg :: ", err)
        os.chdir(current_dir)
        sys.exit(1)

def install(current_dir: str, aurhelper: str, sudo: str):
    packages = ""
    with open(f"{current_dir}/src/pkg/aur.ini", "r") as file:
        for line in file:
            if not line.startswith("[") and not line.startswith("#") and line.strip() != "":
                packages += f"{line.rstrip()} "
    cmd = f"sudo {aurhelper} -S --noconfirm {packages}"
    try:
        subprocess.run(cmd, shell=True, input=sudo, check=True, text=True)
        logging.info(cmd)
        print(":: [+] AUR :: Install")
    except Exception as err:
        logging.error(f"{cmd}: {repr(err)}")
        print(":: [-] AUR :: Install :: ", err)
        sys.exit(1)

def remove(aur_dir: str):
    try:
        os.rmdir(aur_dir)
        logging.info(f"Removing {aur_dir}")
        print(":: [+] AUR :: Rmdir")
    except Exception as err:
        logging.error(f"Cannot remove {aur_dir}\n{err}")
        print(":: [-] AUR :: Rmdir")
