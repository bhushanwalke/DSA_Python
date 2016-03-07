__author__ = 'bhushan'
from Stack import Stack

def dec_to_bin(num):
    print("asd")
    s = Stack()

    while num>0:
        rem = num % 2
        print rem
        if rem == 1:
            s.push('1')
        else:
            s.push('0')
        num = num/2

    bin_num = ""
    while not s.is_empty():
        bin_num += (s.pop())

    return bin_num

print dec_to_bin(3)