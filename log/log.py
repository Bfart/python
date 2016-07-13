#! /usr/bin/python3.5
import logging
import sys

LEVELS = {'debug':logging.DEBUG,'info':logging.INFO,'warning':logging.WARNING,'error':logging.ERROR,'critical':logging.CRITICAL};

if len(sys.argv) > 1:
    levelName = sys.argv[1]
    level = LEVELS.get(levelName,logging.NOTSET)
    logging.basicConfig(level = level)

logging.debug('this is a debug message')
logging.info('this is a info message')
logging.warning('this is a warning message')
logging.error('this is a error message')
logging.critical('this is a critical message')
