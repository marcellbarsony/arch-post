import logging
import os
import subprocess
import sys


"""
Docstring for setting up Python virtual environments
https://wiki.archlinux.org/title/python
https://wiki.archlinux.org/title/python/virtual_environment
https://docs.python.org/3/tutorial/venv.html
"""

def chdir(user: str, dir: str):
    dir = f"/home/{user}/{dir}"
    if os.path.exists(dir):
        os.chdir(dir)
        logging.info(dir)

def venv_init():
        cmd = "python -m venv .venv"
        try:
            subprocess.run(cmd, shell=True, check=True)
            logging.info(cmd)
            print(":: [+] Venv init")
        except subprocess.CalledProcessError as err:
            logging.error(err)
            print(":: [-] Venv init", err)

def venv_activate():
    cmd = "source .venv/bin/activate"
    try:
        subprocess.run(cmd, shell=True, check=True)
        logging.info(cmd)
        print(":: [+] Venv activate")
    except subprocess.CalledProcessError as err:
        logging.error(err)
        print(":: [-] Venv activate", err)

def pip_upgrade():
    cmd = "pip install --upgrade pip"
    try:
        subprocess.run(cmd, shell=True, check=True)
        logging.info(cmd)
        print(":: [+] Pip upgrade")
    except subprocess.CalledProcessError as err:
        logging.error(err)
        print(":: [-] Pip upgrade", err)

def pip_install():
    cmd = "python -m pip install -r requirements.txt"
    try:
        subprocess.run(cmd, shell=True, check=True)
        logging.info(cmd)
        print(":: [+] Pip install")
    except subprocess.CalledProcessError as err:
        logging.error(err)
        print(":: [-] Pip install", err)

def venv_deactivate():
    cmd = "deactivate"
    try:
        subprocess.run(cmd, shell=True, check=True)
        logging.info(cmd)
        print(":: [+] Venv deactivate")
    except subprocess.CalledProcessError as err:
        logging.error(err)
        print(":: [-] Venv deactivate", err)

def pip_install_debugpy():
    cmd = "python -m pip install debugpy"
    try:
        subprocess.run(cmd, shell=True, check=True)
        logging.info(cmd)
        print(":: [+] Pip install debugpy")
    except subprocess.CalledProcessError as err:
        logging.error(err)
        print(":: [-] Pip install debugpy", err)
