import logging
import os
import shutil

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Rust():

    """Docstring for Rust config"""

    def __init__(self):
        pass

    @staticmethod
    def cargo_cfg(user: str):
        """Move Cargo config to $CARGO_HOME"""
        src = f'/home/{user}/.cargo'
        dst = f'/home/{user}/.local/share/cargo'

        if os.path.exists(src) and os.path.isdir(src):
            shutil.move(src, dst)
