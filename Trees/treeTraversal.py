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


def inorder(tree):
    if tree!= None:
        inorder(tree.get_left_child())
        val = tree.get_root_val()
        print(val)
        inorder(tree.get_right_child())

maxValue = None
def findMax(tree):
    global maxValue
    if tree!=None:
        if tree.get_root_val() > maxValue:
            maxValue = tree.get_root_val()
        findMax(tree.get_left_child())
        findMax(tree.get_right_child())
    return maxValue

found = False
def findData(tree, data):
    if tree != None:
        if tree.get_root_val() == data:
            return True

        findData(tree.get_left_child(), data)
        findData(tree.get_right_child(), data)
    return False


q = []
def findDataQueue(tree, data):
    found = False
    if tree!= None:
        q.append(tree)
        while len(q) !=0:
            node = q.pop()
            if node.get_root_val() == data:
                found = True
            if node.get_left_child() != None:
                q.insert(0, node.get_left_child())
            if node.get_right_child() != None:
                q.insert(0, node.get_right_child())
    return found

def size(tree):
    if not tree:
        return 0
    return size(tree.get_left_child()) + size(tree.get_right_child()) + 1


r = BinaryTree('a')
r.insert_left('b')
r.insert_right('c')
r.get_left_child().insert_left('d')
r.get_left_child().insert_right('e')
r.get_right_child().insert_left('f')
r.get_right_child().insert_right('g')
#
# preorder(r)
# print("\n")
# postorder(r)
# print("\n")
# #inorder(r)
# r.inorder()

# print findMax(r)
print findData(r, 'e')
print findDataQueue(r, 'q')
print size(r)
