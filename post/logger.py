import logging
import logging.config


class LogHelper():

    """Docstring for LogHelper"""

    def __init__(self):
        logging.config.fileConfig('post/logging.conf')
        self.logger = logging.getLogger()

    def info(self, message :str) -> None:
        self.logger.setLevel(logging.INFO)
        self.logger.info(message)

    def error(self, message :str) -> None:
        self.logger.setLevel(logging.ERROR)
        self.logger.error(message)

    def warning(self, message :str) -> None:
        self.logger.setLevel(logging.WARNING)
        self.logger.warning(message)

