__author__ = 'bhushan'

class BinaryTree:

    def __init__(self, root):
        self.value = root
        self.left_child = None
        self.right_child = None

    def insert_left(self, new_node):
        if self.left_child == None:
            self.left_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.left_child = self.left_child
            self.left_child = t
            print "\n"

    def insert_right(self, new_node):
        if self.right_child == None:
            self.right_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.right_child = self.right_child
            self.right_child = t

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child


    def get_root_val(self):
        return self.value

    def set_root_val(self, new_val):
        self.value = new_val


r = BinaryTree('a')
r.insert_left('b')
r.insert_right('c')
r.get_left_child().insert_right('d')
print "\n"