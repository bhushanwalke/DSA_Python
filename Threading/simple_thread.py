__author__ = 'bhushan'

import threading, random
import time


def splitter(words, s):
    myList = words.split()
    newList = []
    while (myList):
        newList.append(myList.pop(random.randrange(0, len(myList))))
    time.sleep(s)
    print(' '.join(newList))


if __name__ == '__main__':
    sentence = "I am a handsome devil."
    numOfThread = 5
    threadList = []

    print("Starting\n")
    for i in range(numOfThread):
        t = threading.Thread(target=splitter, args=(sentence,i,))

        t.start()
        threadList.append(t)

    print("\n Thread Count:" + str(threading.activeCount()))
    print("Exiting\n")