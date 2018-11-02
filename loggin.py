# coding:utf-8
import logging
from logging import Formatter
import time


class APP:
    def __init_(self):
        FORMAT = "%(asctime)-15s %(levelname)-8s %(filename)-16s %(message)s"
        formatter = Formatter(fmt=FORMAT)
        logger = logging.getLogger()

        handler = logging.StreamHandler()
        logger.setLevel(logging.DEBUG)

        handler.setFormatter(formatter)
        logger.addHandler(handler)





if __name__ == '__main__':
    app = APP()
    while True:
        test_log()
        time.sleep(1)
