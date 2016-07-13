#!/usr/bin/python3.5

import logging

logging.basicConfig(level=logging.DEBUG,format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',datefmt='%m-%d %H:%M',filename='./myapp.log',filemode='w')

console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)-12s:%(levelname)-8s %(message)s')

console.setFormatter(formatter)

logging.getLogger('').addHandler(console)

logging.info("this is a info message")

logger1 = logging.getLogger('myapp.1111')
logger2 = logging.getLogger('myapp.2222')
logger1.debug('this is a debug message')
logger1.info('this is a logger1.info message')

