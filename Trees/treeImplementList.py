__author__ = 'bhushan'

"""
Tree implementation using list in python
"""

def binary_tree(r):
    return [r, [], []]


def insert_left(root, new_branch):
    t = root.pop(1)
    print "left node {} inserted after {} which had {}".format(new_branch, root, t)
    if len(t) > 1:
        root.insert(1, [new_branch, t, []])
    else:
        root.insert(1, [new_branch, [], []])


def insert_right(root, new_branch):
    t = root.pop(2)
    print "right node {} inserted after {} which had {}".format(new_branch, root, t)
    if len(t) > 1:
        root.insert(2, [new_branch, t, []])
    else:
        root.insert(2, [new_branch, [], []])


def get_root_val(root):
    return root[0]

def set_root_val(root, new_val):
    root[0] = new_val

def get_left_child(root):
    return root[1]

def get_right_child(root):
    return root[2]


def build_tree():
    r = binary_tree('a')
    insert_left(r, 'b')
    insert_right(r, 'c')
    insert_right(r[1], 'd')
    insert_left(r[2], 'e')
    insert_right(r[2], 'f')

    return r

r = binary_tree(3)
insert_left(r, 4)
insert_left(r, 5)
insert_right(r, 6)
insert_right(r, 7)
l = get_left_child(r)
print(l)
set_root_val(l, 9)
print(r)
insert_left(l, 11)
print(r)
print(get_right_child(r))
print(get_right_child(get_right_child(r)))

print build_tree()

['a',
 ['b',
  [], ['d', [], []]],
 ['c',
  ['e', [], []], ['f', [], []]]
 ]