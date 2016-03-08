__author__ = 'bhushan'

from Deques import Deques

def check_palim(string):
    dq = Deques()

    for ch in string:
        dq.add_rear(ch)

    still_equals = True

    while dq.size() > 1 and still_equals:
        if dq.remove_rear() != dq.remove_front():
            still_equals = False


    return still_equals


print check_palim("bhushan")
print check_palim("toot")