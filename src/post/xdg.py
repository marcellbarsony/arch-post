import logging
import os
import shutil


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
                    logging.info(f"XDG: Remove directory - {path}")
                except OSError as err:
                    logging.error(f"XDG: Remove directory - {path}: {err}")

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
                logging.info(f"XDG: Remove file - {path}")

    def move_rust(self):
        cargo_conf = f"{self.home}/.cargo"
        cargo_home = f"{self.home}/.local/share/cargo"
        if os.path.exists(cargo_conf):
            shutil.move(cargo_conf, cargo_home)
            logging.info(f"XDG Rust: Move Cargo {cargo_conf} >> {cargo_home}")

        rustup_conf = f"{self.home}/.rustup"
        rustup_home = f"{self.home}/.local/share/rustup"
        if os.path.exists(rustup_home):
            shutil.move(rustup_conf, rustup_home)
            logging.info(f"XDG Rust: Move Rustup {rustup_conf} >> {rustup_home}")

    def remove_self(self):
        path = f"{self.home}/arch-post"
        if os.path.exists(path):
            shutil.rmtree(path)
            logging.info(f"XDG Self: Remove self - {path}")

    # Remove orphans and their configs (requires root)
    # "sudo pacman -Qtdq | pacman -Rns -"
