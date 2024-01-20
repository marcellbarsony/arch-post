import logging
import os
import shutil
import subprocess
import sys
from .bitwarden import Bitwarden


class SSHagent():

    """
    SSH Agent setup
    https://wiki.archlinux.org/title/SSH_keys
    """

    def __init__(self, user: str, current_dir: str):
        self.user = user
        self.sshdir = f"{current_dir}/src/ssh"

    def config(self):
        src = f"{self.sshdir}/config"
        dst = f"/home/{self.user}/.ssh/"
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

    def service_set(self):
        src = f"{self.sshdir}/ssh-agent.service"
        dst = f"/home/{self.user}/.config/systemd/user/"
        try:
            os.makedirs(dst, exist_ok=True)
            logging.info(f"mkdir {dst}")
            shutil.copy(src, dst)
            logging.info(f"copy {src} >> {dst}")
        except Exception as err:
            logging.error(err)
            sys.exit(1)

    def service_start(self):
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

    def key_gen(self, ssh_key: str, gh_mail: str):
        gh_mail = Bitwarden().rbw_get("github", gh_mail)
        file = f"/home/{self.user}/.ssh/id_ed25519"
        cmd = f"ssh-keygen -q -t ed25519 -N {ssh_key} -C {gh_mail} -f {file}"
        try:
            subprocess.run(cmd, shell=True, check=True)
            logging.info(cmd)
        except subprocess.CalledProcessError as err:
            logging.error(f"{cmd}: {err}")
            sys.exit(1)

    @staticmethod
    def key_add():
        cmd = "ssh-add -q ~/.ssh/id_ed25519"
        try:
            subprocess.run(cmd, shell=True, check=True)
            logging.info(cmd)
        except subprocess.CalledProcessError as err:
            logging.error(f"{cmd}: {err}")
            sys.exit(1)
