from treeTraversal import *
import Queue

r1 = BinaryTree('1')
r = BinaryTree('a')
# r.insert_left(1)
# r.insert_right(3)
r.insert_left('b')
r.insert_right('c')
r.get_left_child().insert_left('d')
r.get_left_child().insert_right('e')
r.get_right_child().insert_left('f')
r.get_right_child().insert_right('g')

def find_height_recursive(root):
    if root == None:
        return -1
    return max(find_height_recursive(root.get_left_child()), find_height_recursive(root.get_right_child())) + 1

print find_height_recursive(r)
print find_height_recursive(r1)


def find_height(root):
    q = Queue.Queue()
    if root == None:
        return 0

    q.put(root)
    height = -1
    while True:
        node_len = q.qsize()
        if node_len == 0:
            return height

        height += 1

        while node_len > 0:
            node = q.get()
            if node.get_left_child() is not None:
                q.put(node.get_left_child())
            if node.get_right_child() is not None:
                q.put(node.get_right_child())

            node_len -= 1

print find_height(r)
print find_height(r1)

