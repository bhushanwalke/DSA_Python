from treeTraversal import *
import Queue
from Stack import Stack

r = BinaryTree('a')
r.insert_left('b')
r.insert_right('c')
r.get_left_child().insert_left('d')
r.get_left_child().insert_right('e')
r.get_right_child().insert_left('f')
r.get_right_child().insert_right('g')

def spiralTraversal(root):
    if root == None:
        return
    even = Stack.Stack()
    odd = Stack.Stack()

    even.push(root)

    while(not even.is_empty() or not odd.is_empty()):
        while(not even.is_empty()):
            node = even.pop()
            print node.get_root_val()

            if node.get_right_child() is not None:
                odd.push(node.get_right_child())
            if node.get_left_child() is not None:
                odd.push(node.get_left_child()) 

        while not odd.is_empty():
            node = odd.pop()
            print node.get_root_val()

            if node.get_left_child() is not None:
                even.push(node.get_left_child())
            if node.get_right_child() is not None:
                even.push(node.get_right_child())
        print "\n"

spiralTraversal(r)
