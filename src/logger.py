import logging
import sys

def setup_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    ch = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter('[%(levelname)s] %(name)s - %(message)s')
    ch.setFormatter(formatter)

    logger.addHandler(ch)
    return logger

if __name__ == "__main__":
    logger = setup_logger(__name__)
    logger.info("Pipeline started")
