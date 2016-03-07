from Stack import Stack
def rev_str(str):
    s = Stack()
    for i in str:
        s.push(i)
    rev = ""
    while not s.is_empty():
        rev += s.pop()
    return rev

# print rev_str("bhushan")
