import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Ruby():

    """
    Docstring for Ruby lang
    https://wiki.archlinux.org/title/ruby
    """

    @staticmethod
    def install():
        logger.info('[TODO] Ruby install')
            #cmd = 'sudo pacman -S ruby rubygems'
            #try:
            #    subprocess.run(cmd, shell=True, check=True)
            #    logger.info('Ruby install')
            #except Exception as err:
            #    logger.error(f'Ruby install {err}')
            #    sys.exit(1)
        pass

    @staticmethod
    def gems():
        logger.info('[TODO] Ruby gems')
            # cd ${HOME}/.local/git/blog
            # gem update
            # gem install jekyll bundler
            # bundle update
            # cd ${HOME}
        pass
