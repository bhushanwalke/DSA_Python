from treeTraversal import *
import Queue

r = BinaryTree('a')
# r.insert_left(1)
# r.insert_right(3)
r.insert_left('b')
r.insert_right('c')
r.get_left_child().insert_left('d')
r.get_left_child().insert_right('e')
r.get_right_child().insert_left('f')
r.get_right_child().insert_right('g')


# r.inorder()


def levelorder(root):
    res = []
    if root is None:
        return res
    q = Queue.Queue()
    q.put(root)
    node = None

    while not q.empty():
        node = q.get()
        res.append(node.get_root_val())
        if node.get_left_child() is not None:
            q.put(node.get_left_child())

        if node.get_right_child() is not None:
            q.put(node.get_right_child())

    return res

print levelorder(r)
