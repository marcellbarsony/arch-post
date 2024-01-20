import logging
import os
import subprocess
import sys


class AURhelper():

    """AUR helper setup"""

    def __init__(self, user: str, aur_helper: str):
        self.user = user
        self.aur_helper = aur_helper
        self.aur_dir = f"/home/{self.user}/.local/src/{self.aur_helper}/"

    def make_dir(self):
        os.makedirs(self.aur_dir, exist_ok=True)
        logging.info(self.aur_dir)

    def clone(self):
        cmd = f"git clone https://aur.archlinux.org/{self.aur_helper}.git {self.aur_dir}"
        try:
            subprocess.run(cmd, shell=True, check=True, stdout=subprocess.DEVNULL)
            logging.info(cmd)
        except subprocess.CalledProcessError as err:
            if err.returncode == 128:
                logging.info(f"Directory already exists: {self.aur_dir}")
            else:
                logging.error(f"{cmd}: {repr(err)}")
                sys.exit(1)

    def make_pkg(self):
        current_dir = os.getcwd()
        cmd = f"makepkg -si --noconfirm"
        try:
            os.chdir(self.aur_dir)
            logging.info(f"os.chdir {self.aur_dir}")
            subprocess.run(cmd, shell=True, check=True, stdout=subprocess.DEVNULL)
            logging.info(cmd)
            os.chdir(current_dir)
            logging.info(f"os.chdir {current_dir}")
        except subprocess.CalledProcessError as err:
            logging.error(f"{cmd}: {repr(err)}")
            os.chdir(current_dir)
            sys.exit(1)

    @staticmethod
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
