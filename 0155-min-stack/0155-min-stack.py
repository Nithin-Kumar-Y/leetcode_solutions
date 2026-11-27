class MinStack(object):

    def __init__(self):
        self.stack= []
        self.r= False
        self.small = 2**31
    def push(self, value):
        """
        :type value: int
        :rtype: None
        """
        if value< self.small:
            self.small = value
        self.stack.append(value)

    def pop(self):
        """
        :rtype: None
        """
        x= self.stack.pop()
        if x> self.small:
            pass
        else:
            self.r= True

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if self.r==True:
            self.small = min(self.stack)
            self.r= False
        return self.small


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()