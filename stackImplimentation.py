class Node:
    def __init__(self, val):
        self.val = val
        self.parent = None

    def __str__(self):
        return str(self.val)


class LinklistStack:
    def __init__(self):
        self.top = None
        self.element = 0

    def push(self, val):
        temp = Node(val)
        if self.top is None:
            self.top = temp
        else:
            temp.parent = self.top
            self.top = temp
        self.element += 1

    def pop(self):
        if self.top is None:
            raise IndexError
        temp = self.top.val
        self.top = self.top.parent
        self.element -= 1
        return temp

    def getLength(self):
        return self.element

    def peek(self):
        if self.top is None:
            return None
        return self.top.val

    def isEmpty(self):
        return True if self.top is None else False

class ArrayStack:
    def __init__(self):
        self.data = []

    def push(self, val):
        self.data.append(val)

    def pop(self):
        return self.data.pop(len(self.data)-1)

    def isEmpty(self):
        return True if len(self.data) == 0 else False


