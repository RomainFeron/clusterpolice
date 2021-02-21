import logging


def setup_logging():

    # Setup logging
    logging.basicConfig(level=logging.INFO,
                        format='[%(asctime)s]::%(levelname)-6s  %(message)s',
                        datefmt='%Y.%m.%d - %H:%M:%S')
