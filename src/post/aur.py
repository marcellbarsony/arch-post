import logging
import os
import subprocess
import sys


"""AUR helper setup"""

def mkdir(aur_dir: str):
    os.makedirs(aur_dir, exist_ok=True)
    logging.info(aur_dir)

def clone(aur_dir: str, aur_helper: str):
    cmd = ["git", "clone", f"https://aur.archlinux.org/{aur_helper}.git", aur_dir]
    try:
        subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL)
    except subprocess.CalledProcessError as err:
        if err.returncode == 128:
            logging.info(f"Directory already exists: {aur_dir}")
            pass
        else:
            logging.error("%s\n%s", cmd, err)
            sys.exit(1)
    else:
        logging.info(cmd)

def mkpkg(aur_dir: str, cwd: str):
    cmd = ["makepkg", "-rsi", "--noconfirm"]
    try:
        os.chdir(aur_dir)
        subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL)
    except subprocess.CalledProcessError as err:
        os.chdir(cwd)
        logging.error("%s\n%s", cmd, err)
        sys.exit(1)
    else:
        os.chdir(cwd)
        logging.info(cmd)
        os.system("clear")

def get_packages(current_dir: str) -> str:
    packages = ""
    with open(f"{current_dir}/src/pkg/aur.ini", "r") as file:
        for line in file:
            if not line.startswith("[") and not line.startswith(";") and line.strip() != "":
                packages += f"{line.rstrip()} "
    return packages

def install(package:str):
    cmd = ["paru", "-S", "--sudoloop", "--noconfirm", package]
    try:
        subprocess.run(cmd, check=True, text=True)
    except Exception as err:
        logging.warning("%s\n%s", cmd, err)
        return
    else:
        logging.info(cmd)
        os.system("clear")

def remove(aur_dir: str):
    try:
        os.rmdir(aur_dir)
    except Exception as err:
        logging.error("%s\n%s", aur_dir, err)
        pass
    else:
        logging.info(aur_dir)
