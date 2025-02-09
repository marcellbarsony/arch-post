import getpass
import logging
import os
import subprocess
import sys


def change():
    os.system("clear")
    cmd = "chsh -s /usr/bin/zsh"
    try:
        subprocess.run(cmd, shell=True, check=True)
    except subprocess.CalledProcessError as err:
        logging.error(f"{cmd}\n{err}")
        sys.exit(1)
    else:
        logging.info(cmd)

def config():
    src = f"/home/{getpass.getuser()}/.config/zsh/global/"
    dst = "/etc/zsh/"
    for file in os.listdir(src):
        src_file = os.path.join(src, file)
        dst_file = os.path.join(dst, file)
        cmds = [
            f"sudo cp -r {src_file} {dst_file}",
            f"sudo chmod 644 {dst_file}"
        ]
        for cmd in cmds:
            try:
                subprocess.run(cmd, shell=True, check=True)
            except subprocess.CalledProcessError as err:
                logging.error(f"{cmd}\n{err}")
                sys.exit(1)
            else:
                logging.info(cmd)

def tools():
    repos = {"marlonrichert/zsh-autocomplete": "zsh-autocomplete"}
    for repo, dir in repos.items():
        dst = f"/home/{getpass.getuser()}/.local/src/{dir}"
        cmd = f"git clone --depth 1 git@github.com:{repo}.git {dst}"
        try:
            subprocess.run(cmd, shell=True, check=True)
        except subprocess.CalledProcessError as err:
            logging.error(f"{cmd}\n{err}")
            sys.exit(1)
        else:
            logging.info(cmd)
