__author__ = 'bhushan'
from Stack import Stack

def check_paren(symbols):
    s = Stack()
    balanced = True
    index = 0

    while index < len(symbols) and balanced:
        symbol = symbols[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.is_empty():
                balanced = False
            else:
                popped = s.pop()
                #print(popped)
                opens = "([{"
                closes = ")]}"
                if opens.index(popped) == closes.index(symbol):
                    balanced = True
                else:
                    balanced = False

        index += 1

    if s.is_empty() and balanced:
        return True
    else:
        return False


# print check_paren("((({[]})))")
# print check_paren("((()")
# print check_paren("((()))(")

