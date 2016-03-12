__author__ = 'bhushan'

def list_sum(num_list):
    if len(num_list) == 1:
        return num_list[0]
    else:
        return num_list[0] + list_sum(num_list[1:])

print list_sum([1,2,3,4,5])


def to_str(n, base):
    convert_string = "0123456789ABCDEF"
    if n < base:
        return convert_string[n]
    else:
        return to_str(n/base, base) + convert_string[n % base]

print to_str(4, 2)
print to_str(10, 2)


def palindrome(string):
    if len(string) <= 1:
        return string
    else:
         new_string = string[len(string)-1] + palindrome(string[:len(string)-1])


print palindrome("asa")
