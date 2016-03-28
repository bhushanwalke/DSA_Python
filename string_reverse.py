__author__ = 'bhushan'


s = "A B C D"
li = s.split()
size = len(li)

def reverse(li, size):
    for i in range(0, size/2):
        li[i], li[size-1-i] = li[size-1-i], li[i]


reverse(li, size)
print li