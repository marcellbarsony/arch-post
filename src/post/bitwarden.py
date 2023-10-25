import logging
import os
import subprocess
import sys


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Bitwarden():

    """Bitwarden-rbw setup"""

    @staticmethod
    def install(aur_helper: str):
        cmd = f"{aur_helper} -S --noconfirm rbw"
        try:
            subprocess.run(cmd, shell=True, check=True)
            logger.info("RBW install")
        except subprocess.CalledProcessError as err:
            logger.error(f"RBW install {err}")
            sys.exit(1)

    @staticmethod
    def register(mail: str, timeout: str):
        while True:
            error = False
            commands = [
                f"rbw config set email {mail}",
                f"rbw config set lock_timeout {timeout}",
                "rbw register",
                "rbw sync"
            ]
            for cmd in commands:
                try:
                    subprocess.run(cmd, shell=True, check=True)
                except KeyboardInterrupt:
                    logger.error("User interrupt")
                    sys.exit(1)
                except subprocess.CalledProcessError as err:
                    logger.error(f"RBW config {err}")
                    error=True
            if error:
                continue
            break

    @staticmethod
    def rbw_get(name: str, item: str) -> str:
        cmd = f'rbw get {name} --full | grep "{item}" | cut -d " " -f 2'
        out = subprocess.run(cmd, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding="UTF-8")
        if "ERROR" in str(out.stderr):
            logger.error(f"Fetch data <{name}> <{item}>")
            sys.exit(1)
        logger.info(f"Fetch data <{name}> <{item}>")
        return out.stdout.rstrip("\n")
