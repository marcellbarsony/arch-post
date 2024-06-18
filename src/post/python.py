import logging
import os
import subprocess


"""
Docstring for Python virtual environments
https://wiki.archlinux.org/title/python#virtual_environment
https://docs.python.org/3/tutorial/venv.html
"""

def chdir(home: str, dir: str):
    dir = f"{home}/{dir}"
    if os.path.exists(dir):
        os.chdir(dir)
        logging.info(dir)

def venv_init():
    cmd = "python -m venv .venv"
    try:
        subprocess.run(cmd, shell=True, check=True)
        print(":: [+] Venv init")
        logging.info(cmd)
    except subprocess.CalledProcessError as err:
        print(":: [-] Venv init", err)
        logging.error(err)

def venv_activate():
    cmd = "source .venv/bin/activate"
    try:
        subprocess.run(cmd, shell=True, check=True)
        print(":: [+] Venv activate")
        logging.info(cmd)
    except subprocess.CalledProcessError as err:
        print(":: [-] Venv activate", err)
        logging.error(err)

def pip_upgrade():
    cmd = "pip install --upgrade pip"
    try:
        subprocess.run(cmd, shell=True, check=True)
        print(":: [+] Pip upgrade")
        logging.info(cmd)
    except subprocess.CalledProcessError as err:
        print(":: [-] Pip upgrade", err)
        logging.error(err)

def pip_install():
    cmd = "python -m pip install -r requirements.txt"
    try:
        subprocess.run(cmd, shell=True, check=True)
        print(":: [+] Pip install")
        logging.info(cmd)
    except subprocess.CalledProcessError as err:
        print(":: [-] Pip install", err)
        logging.error(err)

def venv_deactivate():
    cmd = "deactivate"
    try:
        subprocess.run(cmd, shell=True, check=True)
        print(":: [+] Venv deactivate")
        logging.info(cmd)
    except subprocess.CalledProcessError as err:
        print(":: [-] Venv deactivate", err)
        logging.error(err)

def pip_install_debugpy():
    cmd = "python -m pip install debugpy"
    try:
        subprocess.run(cmd, shell=True, check=True)
        print(":: [+] Pip install debugpy")
        logging.info(cmd)
    except subprocess.CalledProcessError as err:
        print(":: [-] Pip install debugpy", err)
        logging.error(err)
