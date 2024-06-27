import logging
import os
import subprocess


"""
Docstring for Python virtual environments + Debugpy
https://wiki.archlinux.org/title/python#virtual_environment
https://docs.python.org/3/tutorial/venv.html
"""

def chdir(home: str, dir: str):
    dir = f"{home}/{dir}"
    if not os.path.exists(dir):
        os.makedirs(dir)
        logging.info(dir)
    os.chdir(dir)

def venv_init():
    cmd = "python -m venv .venv"
    try:
        subprocess.run(cmd, shell=True, check=True)
        logging.info(cmd)
        print(":: [+] Venv init")
    except subprocess.CalledProcessError as err:
        logging.error(err)
        print(":: [-] Venv init ", err)

def venv_init_debugpy():
    cmd = "python -m venv debugpy"
    try:
        subprocess.run(cmd, shell=True, check=True)
        logging.info(cmd)
        print(":: [+] Venv init [Debugpy]")
    except subprocess.CalledProcessError as err:
        logging.error(err)
        print(":: [-] Venv init [Debugpy] ", err)

def venv_activate():
    cmd = "source .venv/bin/activate"
    try:
        subprocess.run(cmd, shell=True, check=True)
        logging.info(cmd)
        print(":: [+] Venv activate")
    except subprocess.CalledProcessError as err:
        logging.error(err)
        print(":: [-] Venv activate ", err)

def pip_upgrade():
    cmd = "pip install --upgrade pip"
    try:
        subprocess.run(cmd, shell=True, check=True)
        logging.info(cmd)
        print(":: [+] Pip upgrade")
    except subprocess.CalledProcessError as err:
        logging.error(err)
        print(":: [-] Pip upgrade ", err)

def pip_install():
    cmd = "python -m pip install -r requirements.txt"
    try:
        subprocess.run(cmd, shell=True, check=True)
        logging.info(cmd)
        print(":: [+] Pip install")
    except subprocess.CalledProcessError as err:
        logging.error(err)
        print(":: [-] Pip install ", err)

def pip_install_debugpy():
    cmd = "python -m pip install debugpy"
    try:
        subprocess.run(cmd, shell=True, check=True)
        logging.info(cmd)
        print(":: [+] Pip install [Debugpy]")
    except subprocess.CalledProcessError as err:
        logging.error(err)
        print(":: [-] Pip install [Debugpy] ", err)

def venv_deactivate():
    cmd = "deactivate"
    try:
        subprocess.run(cmd, shell=True, check=True)
        logging.info(cmd)
        print(":: [+] Venv deactivate")
    except subprocess.CalledProcessError as err:
        logging.error(err)
        print(":: [-] Venv deactivate ", err)
