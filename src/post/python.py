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
    cmd = ["python", "-m", "venv",  ".venv"]
    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as err:
        logging.error("%s\n%s", cmd, err)
    else:
        logging.info(cmd)

def venv_init_debugpy():
    cmd = ["python", "-m", "venv", "debugpy"]
    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as err:
        logging.error("%s\n%s", cmd, err)
    else:
        logging.info(cmd)

def venv_activate():
    cmd = ["source", ".venv/bin/activate"]
    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as err:
        logging.error("%s\n%s", cmd, err)
    else:
        logging.info(cmd)

def pip_install_debugpy():
    cmd = ["python", "-m", "pip", "install", "debugpy"]
    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as err:
        logging.error("%s\n%s", cmd, err)
    else:
        logging.info(cmd)

def venv_deactivate():
    cmd = ["deactivate"]
    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as err:
        logging.error("%s\n%s", cmd, err)
    else:
        logging.info(cmd)
