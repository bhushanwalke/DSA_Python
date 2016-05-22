def append(x, L):
    temp = [x + element for element in L]
    print temp
    return temp

def bitString(n):
    if n == 0: return []
    if n == 1: return ["0", "1"]
    else:
        return (append("0", bitString(n-1)) + append("1", bitString(n-1)))


print bitString(3)
