def grayCode(n):
    """
    :type n: int
    :rtype: List[int]
    """
    res = [0]

    for i in range(n):
        # res += [x + pow(2, i) for x in reversed(res)]
        for x in reversed(res):
            r = (x+ pow(2, i))
            res.append(x + pow(2, i))
    return res

print grayCode(2)
