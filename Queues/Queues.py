

class Queues(object):

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.itmes == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def __str__(self):
        return "\n".join(str(x) for x in self.items)

q = Queues()
print q
q.enqueue(4)
q.enqueue(6)
q.enqueue(1)
q.enqueue('asd')
print "\n", q
q.dequeue()
print "\n", q
