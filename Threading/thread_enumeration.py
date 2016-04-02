__author__ = 'bhushan'


import random
import threading
import time
import logging


logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-10s) %(message)s')


def worker():
    t = threading.currentThread()
    pause = random.randint(1,5)
    logging.debug('Sleeping %s', pause)
    time.sleep(pause)
    logging.debug('ending')
    return


for i in range(3):
    t = threading.Thread(target=worker)
    t.setDaemon(True)
    t.start()


main_thread = threading.currentThread()
print(threading.enumerate())
for t in threading.enumerate():
    if t is main_thread:
        continue
    logging.debug('joining %s', t.getName())
    t.join()