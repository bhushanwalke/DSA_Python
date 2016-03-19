__author__ = 'bhushan'

"""
In a Professional Services organization, there are three levels of employees: fresher (<1 year of experience), professional (1-5 years of experience), expert (>5 years of experience).  There can be n freshers, 5 professionals, and 2 experts.  If a client calls asking for help with troubleshooting a technical problem, the call must be forwarded to a fresher who is free.  If no freshers are available, the call must be placed on wait.  If fresher cannot handle a call, it must be escalated to the professional.  If the professional cannot handle a call, it must be escalated to an expert.
1.    Design classes and data structures for this problem
2.    Implement getCallHandler()
3.    What is the complexity for finding the next available fresher?
4.    What is the complexity for getCallHandler()?

List all assumptions.
"""


from threading import Thread, Condition
import time
import random

FresherQueue = []
Fre_max = 10
ProfessionalQueue = []
Pro_max = 5
ExpertQueue = []
Exp_max = 2

condition = Condition()

class Call(Thread):

    def run(self):
        nums = range(5)
        global FresherQueue
        while True:
            condition.acquire()
            if len(FresherQueue) == Fre_max:
                print "Queue full, wait for fresher"
                condition.wait()
                print "Fresher Available"
            else:
                num = random.choice(nums)
                F = Fresher(num)
                FresherQueue.append(F)
                print "Fresher assigned"
                condition.notify()
                condition.release()
                time.sleep(random.random())

    def getCallHandler(self, num):
        for i in FresherQueue:
            if i.busy == False:
                if i.handle == False:
                    if len(ProfessionalQueue) == Pro_max:
                        print "Queue full, wait for Professional"
                        condition.wait()
                    else:
                        P = Professional(num)
                        ProfessionalQueue.append(P)

        for j in ProfessionalQueue:
            if j.busy == False:
                if j.handle == False:
                    if len(ExpertQueue) == Exp_max:
                        print "Queue full, wait for Expert"
                        condition.wait()
                    else:
                        E = Expert(num)
                        ExpertQueue.append(E)



class Fresher():
    def __init__(self,id):
        self.id = id
        self.busy = False
        self.handle = True

class Professional():
    def __init__(self,id):
        self.id = id
        self.busy = False
        self.handle = True

class Expert():
    def __init__(self,id):
        self.id = id
        self.busy = False

