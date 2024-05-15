import getpass
import logging
import os
import shutil
import subprocess
import sys

"""
SSH Agent setup
https://wiki.archlinux.org/title/SSH_keys
"""

def config(ssh_dir: str):
    src = f"{ssh_dir}/config"
    dst = f"/home/{getpass.getuser()}/.ssh/"
    dst_path = os.path.join(dst, os.path.basename(src))
    try:
        os.makedirs(dst, exist_ok=True)
        logging.info(f"mkdir {dst}")
        shutil.copy(src, dst)
        logging.info(f"copy {src} >> {dst}")
        os.chmod(dst_path, 0o600)
        logging.info(f"chmod {dst_path}")
    except Exception as err:
        logging.error(err)
        sys.exit(1)

def service_set(ssh_dir: str):
    src = f"{ssh_dir}/ssh-agent.service"
    dst = f"/home/{getpass.getuser()}/.config/systemd/user/"
    try:
        os.makedirs(dst, exist_ok=True)
        logging.info(f"mkdir {dst}")
        shutil.copy(src, dst)
        logging.info(f"copy {src} >> {dst}")
    except Exception as err:
        logging.error(err)
        sys.exit(1)

def service_start():
    cmds = [
        "systemctl --user enable ssh-agent.service",
        "systemctl --user start ssh-agent.service"
    ]
    for cmd in cmds:
        try:
            subprocess.run(cmd, shell=True, check=True)
            logging.info(cmd)
        except subprocess.CalledProcessError as err:
            logging.error(f"{cmd}: {err}")
            sys.exit(1)

def key_gen(ssh_key: str, gh_mail: str):
    file = f"/home/{getpass.getuser()}/.ssh/id_ed25519"
    cmd = f"ssh-keygen -q -t ed25519 -N {ssh_key} -C {gh_mail} -f {file}"
    try:
        subprocess.run(cmd, shell=True, check=True)
        logging.info(cmd)
    except subprocess.CalledProcessError as err:
        logging.error(f"{cmd}: {err}")
        sys.exit(1)

def key_add():
    cmd = "ssh-add -q ~/.ssh/id_ed25519"
    try:
        subprocess.run(cmd, shell=True, check=True)
        logging.info(cmd)
    except subprocess.CalledProcessError as err:
        logging.error(f"{cmd}: {err}")
        sys.exit(1)
