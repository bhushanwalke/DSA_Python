__author__ = 'bhushan'

from Node import Node

class UnorderedList(object):

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def add_node(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def size(self):
        count = 0
        current = self.head
        while current != None:
            count += 1
            current = current.get_next()
        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()

        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

            if previous == None:
                self.head = current.get_next()
            else:
                previous.set_next(current.get_next())

    def display(self):
        str1 = ""
        current = self.head
        while current != None:
            print current.get_data()
            current = current.get_next()
            #str1 += "->" + str((current.get_data()))
        #return str1


un = UnorderedList()
un.add_node(24)
un.add_node(54)
un.add_node(31)
un.add_node(89)
un.add_node(18)
un.display()
print un.size()
print un.search(31)