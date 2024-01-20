import logging
import os
import subprocess
import sys


class Rust():

    """
    Rust default toolchain install
    https://rustup.rs/
    """

    @staticmethod
    def toolchain():
        cmd = "rustup default stable"
        try:
            subprocess.run(cmd, shell=True, check=True, stdout=subprocess.DEVNULL)
            logging.info(cmd)
        except subprocess.CalledProcessError as err:
            logging.error(f"{cmd}: {repr(err)}")
            sys.exit(1)
        os.system("clear")
