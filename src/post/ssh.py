import logging
import os
import shutil
import subprocess
import sys

"""
SSH Agent setup
https://wiki.archlinux.org/title/SSH_keys
"""

def config(home: str, ssh_dir: str):
    src = f"{ssh_dir}/config"
    dst = f"{home}/.ssh/"
    dst_path = os.path.join(dst, os.path.basename(src))
    try:
        # Create config directory
        os.makedirs(dst, exist_ok=True)
        logging.info(f"mkdir {dst}")
        # Move config files
        shutil.copy(src, dst)
        logging.info(f"copy {src} >> {dst}")
        # Chmod 600 (rw)
        os.chmod(dst_path, 0o600)
        logging.info(f"chmod {dst_path}")
    except Exception as err:
        logging.error(err)
        print(":: [-] :: SSH :: Config ::", err)
        sys.exit(1)
    else:
        print(":: [+] :: SSH :: Config")

def service_set(home: str, ssh_dir: str):
    src = f"{ssh_dir}/ssh-agent.service"
    dst = f"{home}/.config/systemd/user/"
    try:
        os.makedirs(dst, exist_ok=True)
        logging.info(f"mkdir {dst}")
        shutil.copy(src, dst)
        logging.info(f"copy {src} >> {dst}")
    except Exception as err:
        logging.error(err)
        print(":: [-] :: SSH :: Service set ::", err)
        sys.exit(1)
    else:
        print(":: [+] :: SSH :: Service set")

def service_start():
    services = [
        ["systemctl", "--user", "enable", "ssh-agent.service"],
        ["systemctl", "--user", "start", "ssh-agent.service"]
    ]
    for service in services:
        try:
            subprocess.run(service, check=True)
        except subprocess.CalledProcessError as err:
            logging.error(f"{service}\n{err}")
            print(":: [-] :: SSH :: Service start ::", err)
            sys.exit(1)
        else:
            logging.info(service)
            print(":: [+] :: SSH :: Service start ::", service)

def key_gen(home: str, ssh_key: str, gh_mail: str):
    file = f"{home}/.ssh/id_ed25519"
    cmd = [
        "ssh-keygen",
        "-q", # Silence keygen
        "-t", "ed25519", # Key type
        "-N", ssh_key, # Passphrase
        "-C", gh_mail, # Comment
        "-f", file, # Key file
    ]
    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as err:
        logging.error(f"{cmd}\n{err}")
        print(":: [-] :: SSH :: Key gen ::", err)
        sys.exit(1)
    else:
        logging.info(cmd)
        print(":: [+] :: SSH :: Key gen")

def key_add():
    cmd = ["ssh-add", "-q", "~/.ssh/id_ed25519"]
    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as err:
        logging.error(f"{cmd}\n{err}")
        print(":: [-] :: SSH :: Key add ::", err)
        sys.exit(1)
    else:
        logging.info(cmd)
        print(":: [+] :: SSH :: Key add")
