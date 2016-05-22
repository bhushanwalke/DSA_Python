__author__ = 'bhushan'

from Stack import Stack

def infix_to_post(infix_exp):
    rank = {'*': 3, '/': 3, '+': 2, '-': 2, '(': 1}
    s = Stack()
    postfix_exp = []
    token_list = infix_exp.split()
    print(token_list)

    for token in token_list:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfix_exp.append(token)
        elif token == '(':
            s.push(token)
        elif token == ')':
            top_token = s.pop()
            while top_token != '(':
                #print "top_token in while", top_token
                postfix_exp.append(top_token)
                top_token = s.pop()
        else:
            while (not s.is_empty()) and (rank[s.peek()] >= rank[token]):
                postfix_exp.append(s.pop())

            s.push(token)

    while not s.is_empty():
        postfix_exp.append(s.pop())

    return " ".join(postfix_exp)




# print infix_to_post("A * B + C * D")
print infix_to_post("( A + B ) * ( C + D )")
