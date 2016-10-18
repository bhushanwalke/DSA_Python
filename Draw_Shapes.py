class Canvas:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.data = [[''] * width for i in range(height)]

    def setpixel(self, row, col):
        self.data[row][col] = '*'

    def getpixel(self, row, col):
        return self.data[row][col]

    def display(self):
        print "\n".join(["".join(row) for row in self.data])

    def display1(self, str1):
        print str1

    def display1(self, str1, str2):
        print str2

class Shape:
    def paint(self, canvas): pass

class Rectangle(Shape):
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def hline(self, x, y, w):
        pass

    def vline(self, x, y, h):
        pass

    def paint(self, canvas):
        self.hline(self.x, self.y, self.w)
        self.hline(self.x, self.y + self.h, self.w)
        self.vline(self.x, self.y, self.h)
        self.vline(self.x + self.w, self.y, self.h)

class Square(Rectangle):
    def __init__(self, x, y, size):
        Rectangle.__init__(self, x, y, size, size)



class A:
    def f(self):
        return self.g()

    def g(self):
        return 'A'

class B(A):
    def g(self):
        return 'B'

a = A()
b = B()
print a.f(), b.f()
print a.g(), b.g()
