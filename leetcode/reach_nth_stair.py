def stair(steps):
    if steps < 2:
        return 1
    return stair(steps-1) + stair(steps-2)

print stair(4)

def stairdp(steps):
    res = [None] * (steps+1)
    res[0] = 1
    res[1] = 1

    for i in range(2, steps+1):
        res[i] = res[i-1] + res[i-2]

    return res[steps]


print stairdp(4)

def stairm(steps, ways):
    res = [None] * (steps + 1)
    res[0] = 1
    res[1] = 1

    for s in range(2, steps+1):
        res[s] = 0
        for m in range(1, ways+1):
            if m >= s+1:
                break
            tmp = res[s-m]
            res[s] += res[s-m]

    return res[steps]

print stairm(4, 2)
