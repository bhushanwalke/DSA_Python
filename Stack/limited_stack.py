class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stk = []
        self.minStk = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if len(self.stk) == 0:
            self.stk.append(x)
            self.minStk.append(x)
        elif x <= self.minStk[len(self.minStk) - 1]:
            self.stk.append(x)
            self.minStk.append(x)
        else:
            self.stk.append(x)

    def pop(self):
        """
        :rtype: void
        """
        if self.top() == self.minStk[len(self.minStk) - 1]:
            self.stk.pop()
            self.minStk.pop()
        else:
            self.stk.pop()

    def top(self):
        """
        :rtype: int
        """
        if len(self.stk) > 0:
            return self.stk[len(self.stk) - 1]
        else:
            return 0


    def getMin(self):
        """
        :rtype: int
        """
        if len(self.minStk) > 0:
            return self.minStk[len(self.minStk) - 1]
        else:
            return 0


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-1)

print obj.getMin()
print obj.top()
print obj.pop()
print obj.getMin()
