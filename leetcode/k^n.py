def power(k, n):
    if n == 0:
        return 1
    x = power(k, n/2)
    if n%2 == 0:
        return pow(x ,2)
    else:
        return k*pow(x,2)

print power(2,4)
