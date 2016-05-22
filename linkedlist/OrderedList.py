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
            if current.get_data() == item:
                found = True
            else:
                if current.get_data() > item:
                    stop = True
                else:
                    current = current.get_next()

        return found

    def add(self, item):
        current = self.head
        previous = None
        temp = Node(item)
        stop = False

        while current != None and not stop:
            if current.get_data() > item:
                stop = True
            else:
                previous = current
                current = current.get_next()

        if previous == None:
            temp.set_next(self.head)
            self.head = temp
        else:
            temp.set_next(current)
            previous.set_next(temp)

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

    def Reverse(self, head):
        self.head = head
        if self.head.get_next() is None or self.head is None:
            return self.head
        tail = self.head.get_next()
        self.head.set_next(None)
        newhead = self.Reverse(tail)
        tail.set_next(None)

        return newhead


ol = OrderedList()
ol.add(31)
ol.add(1)
ol.add(50)
ol.display()
ol.remove(31)
ol.display()
a = ol.Reverse(ol.head)
a.display()

