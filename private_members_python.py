class Cup():
    def __init__(self, color):
        self._color = color
        self.__content = None

    def fill(self, beverage):
        self.__content = beverage

    def display(self):
        print '{}cup has {} in it'.format(self._color, self.__content)


#
# c = Cup("red")
# c.fill("tea")
#
# c.display()
#
# c1 = Cup("black")
# c1.display()
#
# c._color = "blue"
# c.__content = "coke"
# c.display()
#
# c.fill("coke")
# c.display()

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

