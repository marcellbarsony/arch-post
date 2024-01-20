import logging
import subprocess
import sys


class Bitwarden():

    """Bitwarden-rbw setup"""

    @staticmethod
    def install(aur_helper: str):
        cmd = f"{aur_helper} -S --noconfirm rbw"
        try:
            subprocess.run(cmd, shell=True, check=True)
            logging.info(cmd)
        except subprocess.CalledProcessError as err:
            logging.error(f"{cmd}: {repr(err)}")
            sys.exit(1)

    @staticmethod
    def register(mail: str, timeout: str):
        commands = [
            f"rbw config set email {mail}",
            f"rbw config set lock_timeout {timeout}",
            "rbw register",
            "rbw sync"
        ]
        error = False
        while True:
            for cmd in commands:
                try:
                    subprocess.run(cmd, shell=True, check=True)
                    logging.info(cmd)
                except KeyboardInterrupt:
                    logging.error("User interrupt")
                    sys.exit(1)
                except subprocess.CalledProcessError as err:
                    logging.error(f"{cmd}: {repr(err)}")
                    error=True
            if error:
                continue
            break

    @staticmethod
    def rbw_get(name: str, item: str) -> str:
        cmd = f'rbw get {name} --full | grep "{item}" | cut -d " " -f 2'
        out = subprocess.run(cmd, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding="UTF-8")
        if "ERROR" in str(out.stderr):
            logging.error(f"{cmd}: {out.stderr}")
            sys.exit(1)
        logging.info(cmd)
        return out.stdout.rstrip("\n")
