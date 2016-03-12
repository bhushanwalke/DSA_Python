from Node import Node


class OrderedList(object):

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def size(self):
        current = self.head
        count = 0
        while self.head != None:
            current = current.get_next()
            count += 1

        return count

    def search(self, item):
        current = self.head
        stop = False
        found = False

        while current != None and not stop and not found:
            if current.get_data() == item
                found = True
            else:
                if current.get_data > item:
                    stop = True
                else:
                    current = current.get_next()

        return found