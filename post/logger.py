import logging
import logging.config


class LogHelper():

    """Docstring for LogHelper"""

    def __init__(self):
        logging.config.fileConfig('post/logging.conf')
        self.logger = logging.getLogger()

    def info(self, message):
        self.logger.info(message)

    def error(self, message):
        self.logger.error(message)

    def warning(self, message):
        self.logger.warning(message)

