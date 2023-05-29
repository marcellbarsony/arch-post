import logging
import os
import subprocess

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Rust():

    """Docstring for Rust setup"""

    @staticmethod
    def install():
        """
        Rust install with Rustup
        https://rustup.rs/
        """
        cmd = "curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh"
        try:
            os.system('clear')
            subprocess.run(cmd, shell=True, check=True)
            logger.info('Rust install')
        except subprocess.CalledProcessError as err:
            logger.error(err)
