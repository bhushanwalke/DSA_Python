__author__ = 'bhushan'

import threading
import time

class AsyncWrite(threading.Thread):
    def __init__(self, text, out):
        threading.Thread.__init__(self)
        self.text = text
        self.out = out

    def run(self):
        f = open(self.out, "a")
        f.write(self.text + '\n')
        f.close()
        time.sleep(2)
        print("Finished writing to " + self.out)

def Main():
    message = raw_input("Enter message")
    background = AsyncWrite(message, 'out.txt')
    background.start()
    print("100 + 400 = ", 100+400 )
    background.join()
    print("waited for thread to complete")



if __name__ == '__main__':
    Main()