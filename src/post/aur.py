import logging
import os
import subprocess
import sys


"""AUR helper setup"""

def make_dir(aur_dir: str):
    os.makedirs(aur_dir, exist_ok=True)
    logging.info(aur_dir)

def clone(aur_dir: str, aur_helper: str):
    cmd = f"git clone https://aur.archlinux.org/{aur_helper}.git {aur_dir}"
    try:
        subprocess.run(cmd, shell=True, check=True, stdout=subprocess.DEVNULL)
        logging.info(cmd)
    except subprocess.CalledProcessError as err:
        if err.returncode == 128:
            logging.info(f"Directory already exists: {aur_dir}")
        else:
            logging.error(f"{cmd}: {repr(err)}")
            sys.exit(1)

def makepkg(aur_dir: str):
    current_dir = os.getcwd()
    cmd = f"makepkg -si --noconfirm"
    try:
        os.chdir(aur_dir)
        logging.info(f"os.chdir {aur_dir}")
        subprocess.run(cmd, shell=True, check=True, stdout=subprocess.DEVNULL)
        logging.info(cmd)
        os.chdir(current_dir)
        logging.info(f"os.chdir {current_dir}")
    except subprocess.CalledProcessError as err:
        logging.error(f"{cmd}: {repr(err)}")
        os.chdir(current_dir)
        sys.exit(1)
    os.system("clear")

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
    except Exception as err:
        logging.error(f"{cmd}: {repr(err)}")
        sys.exit(1)
