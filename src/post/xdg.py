import os
import logging
import shutil
import sys

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


class XDGStandard():

    """Docstring for Cross Desktop Group (XDG)"""

    def __init__(self, user):
        self.home = f"/home/{user}"

    def remove_xdg(self):
        dirs = [
            "Desktop",
            "Documents",
            "Music",
            "Public",
            "Templates",
            "Videos"
        ]
        for dir in dirs:
            path = os.path.join(self.home, dir)
            if os.path.exists(path):
                try:
                    os.rmdir(path)
                    logger.info("Remove XDG", dir)
                except OSError as err:
                    logger.error("Remove XDG", dir, err)

    def remove_home(self):
        files = [
            ".bashrc",
            ".bash_logout",
            ".bash_profile",
            ".bash_history",
            ".gitconfig"
        ]
        for file in files:
            path = os.path.join(self.home, file)
            if os.path.exists(path):
                os.remove(path)
                logger.info("Removed ", file)

    def move_rust(self):
        cargo_conf = f"{self.home}/.cargo"
        cargo_home = f"{self.home}/.local/share/cargo"
        if os.path.exists(cargo_conf):
            logger.info("[i] Moving ", cargo_conf)
            shutil.move(cargo_conf, cargo_home)

        rustup_conf = f"{self.home}/.rustup"
        rustup_home = f"{self.home}/.local/share/rustup"
        if os.path.exists(rustup_home):
            logger.info("[i] Moving ", rustup_conf)
            shutil.move(rustup_conf, rustup_home)

    def remove_self(self):
        path = f"{self.home}/arch-post"
        if os.path.exists(path):
            shutil.rmtree(path)

    # Remove orphans and their configs (requires root)
    # "sudo pacman -Qtdq | pacman -Rns -"
