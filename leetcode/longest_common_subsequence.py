def commonsubsequence(s1, s2):
    l1 = len(s1)
    l2 = len(s2)
    match = [[None] * (l2+1) for x in range(l1+1)]

    for i in range(len(s1)+1):
        for j in range(len(s2)+1):
            if i == 0 or j == 0:
                match[i][j] = 0
                # display(match)
            elif s1[i-1] == s2[j-1]:
                # display(match)
                match[i][j] = match[i-1][j-1] + 1
            else:
                match[i][j] = max(match[i-1][j], match[i][j-1])


    display(match)

def display(match):
    for i in range(len(match)):
        print match[i]
    print "\n"


commonsubsequence('ABCDGH', 'AEDFHR')
