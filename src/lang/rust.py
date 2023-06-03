import logging
import os
import shutil
import subprocess

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Rust():

    """Docstring for Rust setup"""

    def __init__(self, user):
        self.user = user

    @staticmethod
    def toolchain():
        """
        Rust default toolchain install
        https://rustup.rs/
        """
        cmd = "rustup default stable"
        try:
            subprocess.run(cmd, shell=True, check=True)
            logger.info('Toolchain install')
        except subprocess.CalledProcessError as err:
            logger.error(err)
