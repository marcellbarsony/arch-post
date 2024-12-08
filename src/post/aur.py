import logging
import os
import subprocess
import sys


"""AUR helper setup"""

def mkdir(aur_dir: str):
    os.makedirs(aur_dir, exist_ok=True)
    logging.info(aur_dir)
    print(":: [+] :: AUR :: Mkdir")

def clone(aur_dir: str, aur_helper: str):
    cmd = f"git clone https://aur.archlinux.org/{aur_helper}.git {aur_dir}"
    try:
        subprocess.run(cmd, shell=True, check=True, stdout=subprocess.DEVNULL)
    except subprocess.CalledProcessError as err:
        if err.returncode == 128:
            logging.info(f"Directory already exists: {aur_dir}")
        else:
            logging.error(f"{cmd}\n{repr(err)}")
            print(":: [-] :: AUR :: Clone")
            sys.exit(1)
    else:
        logging.info(cmd)
        print(":: [+] :: AUR :: Clone")

def mkpkg(aur_dir: str, cwd: str):
    cmd = f"makepkg -rsi --noconfirm"
    try:
        os.chdir(aur_dir)
        subprocess.run(cmd, shell=True, check=True, stdout=subprocess.DEVNULL)
    except subprocess.CalledProcessError as err:
        os.chdir(cwd)
        logging.error(f"{cmd}\n{repr(err)}")
        print(":: [-] :: AUR :: Makepkg :: ", err)
        sys.exit(1)
    else:
        os.chdir(cwd)
        logging.info(cmd)
        os.system("clear")

def install(current_dir: str, aurhelper: str, sudo: str):
    packages = ""
    with open(f"{current_dir}/src/pkg/aur.ini", "r") as file:
        for line in file:
            if not line.startswith("[") and not line.startswith(";") and line.strip() != "":
                packages += f"{line.rstrip()} "

    cmd = f"sudo {aurhelper} -S --noconfirm {packages}"
    try:
        subprocess.run(cmd, shell=True, input=sudo, check=True, text=True)
    except Exception as err:
        logging.error(f"{cmd}: {repr(err)}")
        print(":: [-] :: AUR :: Install :: ", err)
        sys.exit(1)
    else:
        logging.info(cmd)
        print(":: [+] :: AUR :: Install")

def remove(aur_dir: str):
    try:
        os.rmdir(aur_dir)
    except Exception as err:
        logging.error(f"Cannot remove {aur_dir}\n{err}")
        print(":: [-] :: AUR :: Rmdir :: ", err)
    else:
        logging.info(f"Removing {aur_dir}")
        print(":: [+] :: AUR :: Rmdir")
