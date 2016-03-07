__author__ = 'bhushan'

class Stack(object):
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return "\n".join(str(x) for x in self.items)




# s = Stack()
#
# #print(s.is_empty())
# s.push(2)
# s.push(4)
# s.push('qwe')
# s.push('bhushan')
# s.push(89.45)
#
# # print(s.peek())
# print(s)
