import os
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Finalize():

    """Docstring for Finalize"""

    def __init__(self, user):
        self.user = user

    def clean_home(self):
        files = ['.bash_history', '.bash_logout', '.bash_profile', '.bashrc', '.gitconfig']
        for file in files:
            os.remove(os.path.join(f'/home/{self.user}', file))
            logger.info(f'Removed {file}')

    # Remove orphans and their configs (requires root)
    # 'sudo pacman -Qtdq | pacman -Rns -'
