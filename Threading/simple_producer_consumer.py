__author__ = 'bhushan'

import threading, random, time
from Queue import Queue


class Producer():
    def __init__(self):
        self.food = ['Ham', 'Soup', 'Salad']
        self.nextTime = 0

    def run(self):
        global q
        while(time.clock() < 10):
            if(self.nextTime < time.clock()):
                f = self.food[random.randrange(0, len(self.food))]
                q.put(f)
                print("Adding " + f)
                self.nextTime += random.random()*2


class Consumer():
    def __init__(self):
        self.nextTime = 0

    def run(self):
        global q
        while(time.clock() < 10):
            if self.nextTime < time.clock() and not q.empty():
                f = q.get()
                print("Removing " + f)
                self.nextTime += random.random()*4



if __name__ == '__main__':
    q = Queue(10)

    p = Producer()
    c = Consumer()

    pt = threading.Thread(target=p.run, args=())
    ct = threading.Thread(target=c.run, args=())

    pt.start()
    ct.start()
    print(threading.activeCount())