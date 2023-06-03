import os
import logging
import shutil
import sys


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class XDGStandard():

    """Docstring for Cross Desktop Group (XDG)"""

    def __init__(self, user):
        self.user = user

    @staticmethod
    def xdg_force():
        # cmd = 'LC_ALL=C.UTF-8 xdg-user-dirs-update --force'
        # try:
        #     subprocess.run(cmd, shell=True, check=True)
        #     logger.info('Create XDG dirs')
        # except Exception as err:
        #     logger.error(f'Create XDG dirs {err}')
        #     sys.exit(1)
        pass

    @staticmethod
    def xdg_remove(user: str):
        # Remove directories
        parent = f'/home/{user}'
        dirs = ['Desktop', 'Documents', 'Music', 'Public', 'Templates', 'Videos']
        for dir in dirs:
            path = os.path.join(parent, dir)
            if os.path.exists(path):
                try:
                    os.rmdir(path)
                    logger.info(f'Remove XDG {dir}')
                except OSError as err:
                    logger.error(f'Remove XDG {dir} {err}')
                    sys.exit(1)

    def home(self):
        files = ['.bashrc',
                 '.bash_logout',
                 '.bash_profile',
                 '.bash_history',
                 '.gitconfig']
        for file in files:
            path = os.path.join(f'/home/{self.user}', file)
            if os.path.exists(path):
                os.remove(path)
                logger.info(f'Removed {file}')

    def rust(self):
        cargo_conf = f'/home/{self.user}/.cargo'
        cargo_home = f'/home/{self.user}/.local/share/cargo'
        if os.path.exists(cargo_conf):
            shutil.move(cargo_conf, cargo_home)

        rustup_conf = f'/home/{self.user}/.rustup'
        rustup_home = f'/home/{self.user}/.local/share/rustup'
        if os.path.exists(rustup_home):
            shutil.move(rustup_conf, rustup_home)

    # Remove orphans and their configs (requires root)
    # 'sudo pacman -Qtdq | pacman -Rns -'
