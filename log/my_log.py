# coding:utf-8
import logging
from logging import Formatter
import time
import sys


class APP:
    def __init__(self):
        self.stderr_path = '/dev/null'
        FORMAT = "%(asctime)-15s %(levelname)-8s %(filename)-10s %(message)s"
        formatter = Formatter(fmt=FORMAT)
        logger = logging.getLogger()

        handler = logging.StreamHandler()
        logger.setLevel(logging.DEBUG)

        handler.setFormatter(formatter)
        logger.addHandler(handler)


if __name__ == '__main__':
    app = APP()
    logging.debug('cxtan')
