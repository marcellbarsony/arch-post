import logging


def main(cmd :str) -> None:
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s %(levelname)s %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        #filename='basic.log'
    )

    logging.debug('Debug message')
    logging.info('Info message')
    logging.warning('Warning message')
    logging.error('Error message')
    logging.critical('Critical message')


if __name__ == '__main__':
    cmd = 'ls -al'
    main(cmd)
