__author__ = 'bhushan'

def beautiful_binary_strings(BinaryString):
    res = []
    ca = 0
    cb = 0
    checked = True
    i = 0
    while i < len(BinaryString):
        if BinaryString[i] == 'A':
            if ca == 0:
                res.append(BinaryString[i])
                ca += 1
            else:
                if (res[len(res)-1] == 'A'):
                    res.pop()
                    ca -= 1
                    checked = True
                else:
                    checked = False
                    res.append(BinaryString[i])
                    ca += 1
        else:
            if cb == 0:
                res.append(BinaryString[i])
                cb += 1
            else:
                if (res[len(res)-1] == 'B'):
                    res.pop()
                    cb -= 1
                    checked = True
                else:
                    checked = False
                    res.append(BinaryString[i])
                    cb += 1
        i += 1

    if len(res) == 0 and checked:
        return True
    else:
        return False



print beautiful_binary_strings("ABAB")

