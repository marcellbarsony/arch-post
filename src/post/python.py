import logging
import os
import subprocess
import sys


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
            logging.info(f"Python: chdir - {dir}")

    @staticmethod
    def venv_init():
            cmd = "python -m venv .venv"
            try:
                subprocess.run(cmd, shell=True, check=True)
                logging.info(f"Python: Venv init")
                print("[+] Venv init")
            except subprocess.CalledProcessError as err:
                logging.error(f"Python: Venv init: {err}")
                print("[-] Venv init", err)
                sys.exit(1)

    @staticmethod
    def venv_activate():
        cmd = "source .venv/bin/activate"
        try:
            subprocess.run(cmd, shell=True, check=True)
            logging.info(f"Python: Venv activate")
            print("[+] Venv activate")
        except subprocess.CalledProcessError as err:
            logging.error(f"Python: Venv activate: {err}")
            print("[-] Venv activate", err)
            sys.exit(1)

    @staticmethod
    def pip_upgrade():
        cmd = "pip install --upgrade pip"
        try:
            subprocess.run(cmd, shell=True, check=True)
            logging.info(f"Python: Pip upgrade")
            print("[+] Pip upgrade")
        except subprocess.CalledProcessError as err:
            logging.error(f"Python: Pip upgrade: {err}")
            print("[-] Pip upgrade", err)
            sys.exit(1)

    @staticmethod
    def pip_install():
        cmd = "python -m pip install -r requirements.txt"
        try:
            subprocess.run(cmd, shell=True, check=True)
            logging.info(f"Python: Pip install requirements")
            print("[+] Pip install")
        except subprocess.CalledProcessError as err:
            logging.error(f"Python: Pip install requirements: {err}")
            print("[-] Pip install", err)
            sys.exit(1)

    @staticmethod
    def venv_deactivate():
        cmd = "deactivate"
        try:
            subprocess.run(cmd, shell=True, check=True)
            logging.info(f"Python: Venv deactivate")
            print("[+] Venv deactivate")
        except subprocess.CalledProcessError as err:
            logging.error(f"Python: Venv deactivate: {err}")
            print("[-] Venv deactivate", err)
            sys.exit(1)
