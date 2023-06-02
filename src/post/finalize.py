import os
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Finalize():

    """Docstring for Finalize"""

    def __init__(self, user):
        self.user = user

    def clean_home(self):
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

    # Remove orphans and their configs (requires root)
    # 'sudo pacman -Qtdq | pacman -Rns -'
