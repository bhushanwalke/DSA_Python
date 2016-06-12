def catalan(n):
    if n == 0:
        return 1
    count = 0

    for i in range(1, n+1):
        count += catalan(i-1) * catalan(n-i)

    return count

print catalan(2)
