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
    except subprocess.CalledProcessError as err:
        logging.error(err)
        print(":: [-] :: PYTHON :: Venv init ::", err)
    else:
        logging.info(cmd)
        print(":: [+] :: PYTHON :: Venv init")

def venv_init_debugpy():
    cmd = "python -m venv debugpy"
    try:
        subprocess.run(cmd, shell=True, check=True)
    except subprocess.CalledProcessError as err:
        logging.error(err)
        print(":: [-] :: PYTHON :: Venv init :: Debugpy ::", err)
    else:
        logging.info(cmd)
        print(":: [+] :: PYTHON :: Venv init :: Debugpy")

def venv_activate():
    cmd = "source .venv/bin/activate"
    try:
        subprocess.run(cmd, shell=True, check=True)
    except subprocess.CalledProcessError as err:
        logging.error(err)
        print(":: [-] :: PYTHON :: Venv activate ::", err)
    else:
        logging.info(cmd)
        print(":: [+] :: PYTHON :: Venv activate")

def pip_upgrade():
    cmd = "pip install --upgrade pip"
    try:
        subprocess.run(cmd, shell=True, check=True)
    except subprocess.CalledProcessError as err:
        logging.error(err)
        print(":: [-] :: PYTHON :: Pip upgrade ::", err)
    else:
        logging.info(cmd)
        print(":: [+] :: PYTHON :: Pip upgrade")

def pip_install():
    cmd = "python -m pip install -r requirements.txt"
    try:
        subprocess.run(cmd, shell=True, check=True)
    except subprocess.CalledProcessError as err:
        logging.error(err)
        print(":: [-] :: PYTHON :: Pip install ::", err)
    else:
        logging.info(cmd)
        print(":: [+] :: PYTHON :: Pip install")

def pip_install_debugpy():
    cmd = "python -m pip install debugpy"
    try:
        subprocess.run(cmd, shell=True, check=True)
    except subprocess.CalledProcessError as err:
        logging.error(err)
        print(":: [-] :: PTYHON :: Pip install :: Debugpy ::", err)
    else:
        logging.info(cmd)
        print(":: [+] :: PYTHON :: Pip install :: Debugpy")

def venv_deactivate():
    cmd = "deactivate"
    try:
        subprocess.run(cmd, shell=True, check=True)
    except subprocess.CalledProcessError as err:
        logging.error(err)
        print(":: [-] :: PYTHON :: Venv deactivate ::", err)
    else:
        logging.info(cmd)
        print(":: [+] :: PYTHON :: Venv deactivate")
