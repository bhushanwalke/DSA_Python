import sys
def min_max(a):
    mini = a[0]
    maxi = a[0]

    for i in a:
        if i < mini:
            mini = i
        if i > maxi:
            maxi = i

    return 'min {} max {}'.format(mini, maxi)


print min_max([4,3,34,235,3,4,6])
