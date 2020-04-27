class Node:
    def __init__(self, val, min):
        self.val = val
        self.parent = None
        self.substackMin = min

    def __str__(self):
        return str(self.val)


class LinklistStack:
    def __init__(self):
        self.top = None
        self.minVal = float('inf')

    def push(self, val):
        if val < self.min:
            self.min = val
        temp = Node(val, self.min)
        if self.top is None:
            self.top = temp
        else:
            temp.parent = self.top
            self.top = temp

    def pop(self):
        if self.top is None:
            raise IndexError
        temp = self.top.val
        self.top = self.top.parent
        if self.top.substackMin < self.minVal:
            self.minVal = self.top.substackMin
        return temp

    def getMin(self):
        return self.minVal
    
    def isEmpty(self):
        return True if self.top is None else False
