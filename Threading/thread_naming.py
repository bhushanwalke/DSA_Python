__author__ = 'bhushan'

import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG, format='[%(levelname)s] (%(threadName)-10s) %(message)s')

def worker():
    print threading.currentThread().getName(), "Starting"
    logging.debug("Starting")
    time.sleep(2)
    print threading.currentThread().getName(), "Exiting"


def my_Service():
    print threading.currentThread().getName(), "Starting"
    time.sleep(2)
    print threading.currentThread().getName(), "Exiting"


t = threading.Thread(name="my_Service", target=my_Service)
w = threading.Thread(name="worker", target=worker)
w1 = threading.Thread(target=worker)
w2 = threading.Thread(target=worker)

w.start()
w2.start()
t.start()
w1.start()