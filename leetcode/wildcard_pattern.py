def matchpattern(pattern, target):
    i = 0
    j = 0
    if pattern == None or target == None:
        return False
    while i<len(pattern) and j < len(target):

        if pattern[i] == '*':
            i += 1
            while i<len(pattern):
                while j<len(target):
                    if pattern[i] == target[j]:
                        break
                    j += 1
                break
        elif pattern[i] == '?':
            i += 1
        else:
            if pattern[i] != target[j]:
                return False
        i+=1
        j+=1

    return True



# print matchpattern('a*bc', 'aaaabc')
# # print matchpattern('*aabc', 'aaaaaxaabc')
# print matchpattern('a?b', 'acb')
# print matchpattern('say', 'sayali')
# print matchpattern('abb', 'acb')
# print matchpattern(None, 'acb')
print matchpattern("say*j", "sayali")

# // "say", "sayali" --> true
# // "abc" , "sayali" --> false
# // "li", "sayali" --> true
# //
#
# // NULL, "sayali"
# // "say*i", "sayali" --> true
# // "say*j", "sayali" --> false
# // "*", "sayali" --> true
# // "s?yali", "sayali" --> true
#
# // a*b, aaaaaba
# // *bbbbbx, "bbbbbbbbbbbbbbybbbbbbx"
