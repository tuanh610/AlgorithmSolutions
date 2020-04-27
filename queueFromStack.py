import stackImplimentation

class QueueFromStack():
    def __init__(self):
        self.mainStack = stackImplimentation.LinklistStack()
        self.reserveStack = stackImplimentation.LinklistStack()

    def enqueue(self, val):
        self.mainStack.push(val)

    def dequeue(self):
        while not self.mainStack.isEmpty():
            self.reserveStack.push(self.mainStack.pop())
        temp = self.reserveStack.pop()
        while not self.reserveStack.isEmpty():
            self.mainStack.push(self.reserveStack.pop())
        return temp

    def isEmpty(self):
        return self.mainStack.isEmpty()

a = QueueFromStack()
a.enqueue(5)
a.enqueue(10)
a.enqueue(15)
while not a.isEmpty():
    print(a.dequeue())