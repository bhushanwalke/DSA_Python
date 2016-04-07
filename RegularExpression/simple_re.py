'''
Regular expressions without re library
'''


def isPhoneNumber(text):
    if len(text) != 12:
        return False

    try:
        res = text.split('-')
        #print res
    except:
        return False

    for i in res:
        if not unicode(i).isdecimal():
            return False

    if len(res[0]) != 3:
        return False

    if len(res[1]) != 3:
        return False

    if len(res[2]) != 4:
        return False

    return True

print('415-555-4242 is a phone number:')
print(isPhoneNumber('415-555-4242'))
print('Moshi moshi is a phone number:')
print(isPhoneNumber('Moshi moshiq'))



message = "Call me at 415-555-1011 tomorrow. 415-555-9999 is my office."

for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print "Phone numbers found: " + chunk