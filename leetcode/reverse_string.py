def reverseWords(s):
    """
    :type s: a list of 1 length strings (List[str])
    :rtype: nothing
    """
    s_list = list(s) + [' ']
    f = 0
    for i in range(len(s_list)):
        if s_list[i] == ' ':
            s = i-1
            swap(s_list, f, s)
            f = i+1

    swap(s_list, 0, len(s_list) - 1)
    return ''.join(s_list)

def swap(s_list, f, s):
    while f <= s and s >= f:
        s_list[f], s_list[s] = s_list[s], s_list[f]
        s -= 1
        f += 1
    return




s = "a b"
print reverseWords(s)
