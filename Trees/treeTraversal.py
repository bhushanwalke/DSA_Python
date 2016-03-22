__author__ = 'bhushan'

from treeImplementationNode import BinaryTree

def preorder(tree):
    if tree:
        val = tree.get_root_val()
        print val
        preorder(tree.get_left_child())
        preorder(tree.get_right_child())


def postorder(tree):

    if tree!= None:
        postorder(tree.get_left_child())
        postorder(tree.get_right_child())
        val = tree.get_root_val()
        print(val)



r = BinaryTree('a')
r.insert_left('b')
r.insert_right('c')
r.get_left_child().insert_left('d')
r.get_left_child().insert_right('e')
r.get_right_child().insert_left('f')
r.get_right_child().insert_right('g')

preorder(r)
print("\n")
postorder(r)
print("\n")
r.postorder()