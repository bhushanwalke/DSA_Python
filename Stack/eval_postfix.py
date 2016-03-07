__author__ = 'bhushanwalke'
from Stack import Stack

def do_math(pop1, pop2, token):
    if token == '*':
        return pop2 * pop1
    if token == '/':
        return pop2 / pop1
    if token == '+':
        return pop2 + pop1
    if token == '-':
        return pop2 + pop1


def eval_postfix(pos_exp):
    s = Stack()
    pos_tokens = pos_exp.split()

    for token in pos_tokens:
        if token in "0123456789":
            s.push(int(token))
        else:
            pop1 = s.pop()
            pop2 = s.pop()
            res = do_math(pop1, pop2, token)
            s.push(res)

    return s.pop()


print(eval_postfix('7 8 + 3 2 + /'))