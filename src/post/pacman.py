import logging
import subprocess
import sys


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Pacman():

    """
    Package manager setup
    https://wiki.archlinux.org/title/Pacman/Package_signing
    """

    @staticmethod
    def keyring():
        cmd = "sudo pacman -D --asexplicit archlinux-keyring",
        try:
            subprocess.run(cmd, shell=True, check=True, stdout=subprocess.DEVNULL)
            logger.info("Explicit Keyring")
        except subprocess.CalledProcessError as err:
            logger.error(f"Explicit Keyring {err}")
            sys.exit(1)
