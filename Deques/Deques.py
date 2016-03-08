__author__ = 'bhushan'

class Deques(object):
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def add_rear(self, item):
        self.items.insert(0, item)

    def add_front(self, item):
        self.items.append(item)

    def remove_front(self):
        return self.items.pop()

    def remove_rear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def __str__(self):
        return " ".join(str(x) for x in self.items)

#
# dq = Deques()
# dq.add_rear(4)
# print dq
# dq.add_rear(5)
# print dq

