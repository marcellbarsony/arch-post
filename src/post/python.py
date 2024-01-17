import logging
import os
import subprocess
import sys

logging.basicConfig(level=logging.INFO, filename="archpost.log", filemode="w",
                    format="%(asctime)s - %(levelname)s - %(message)s")

class Python():

    """
    Docstring for setting up Python virtual environments
    https://wiki.archlinux.org/title/python
    https://wiki.archlinux.org/title/python/virtual_environment
    https://docs.python.org/3/tutorial/venv.html
    """

    def __init__(self):
        self.user = os.getlogin()

    def chdir(self, dir: str):
        dir = f"/home/{self.user}/.local/git/{dir}"
        if os.path.exists(dir):
            os.chdir(dir)

    @staticmethod
    def venv_init():
            cmd = "python -m venv .venv"
            try:
                subprocess.run(cmd, shell=True, check=True)
                print("[+] Venv init")
            except subprocess.CalledProcessError as err:
                print("[-] Venv init", err)
                sys.exit(1)

    @staticmethod
    def venv_activate():
        cmd = "source .venv/bin/activate"
        try:
            subprocess.run(cmd, shell=True, check=True)
            print("[+] Venv activate")
        except subprocess.CalledProcessError as err:
            print("[-] Venv activate", err)
            sys.exit(1)

    @staticmethod
    def pip_upgrade():
        cmd = "pip install --upgrade pip"
        try:
            subprocess.run(cmd, shell=True, check=True)
            print("[+] Pip upgrade")
        except subprocess.CalledProcessError as err:
            print("[-] Pip upgrade", err)
            sys.exit(1)

    @staticmethod
    def pip_install():
        cmd = "python -m pip install -r requirements.txt"
        try:
            subprocess.run(cmd, shell=True, check=True)
            print("[+] Pip install")
        except subprocess.CalledProcessError as err:
            print("[-] Pip install", err)
            sys.exit(1)

    @staticmethod
    def venv_deactivate():
        cmd = "deactivate"
        try:
            subprocess.run(cmd, shell=True, check=True)
            print("[+] Venv deactivate")
        except subprocess.CalledProcessError as err:
            print("[-] Venv deactivate", err)
            sys.exit(1)
