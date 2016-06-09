import math
def isprime(num):
    if num == 1:
        return False
    if num == 2:
        return True
    if num == 3:
        return True

    for i in range(2, int(math.sqrt(num))+1):
        if num%i == 0:
            return False
    return True


n = int(raw_input())
for i in range(n):
    r = raw_input().split(" ")
    start, end = int(r[0]), int(r[1])
    c = 0
    for num in range(start, end + 1):
        if isprime(num):
            print num
            c += 1
    print c
