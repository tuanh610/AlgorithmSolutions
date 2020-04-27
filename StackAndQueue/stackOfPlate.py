from stackImplimentation import LinklistStack

class stackOfPlate:
    def __init__(self, maxElements):
        self.stacks = [LinklistStack()]
        self.maxElements = maxElements

    def push(self, val):
        curStack = self.stacks[-1]
        if curStack.getLength() < self.maxElements:
            curStack.push(val)
        else:
            self.stacks.append(LinklistStack())
            self.stacks[-1].push(val)

    def pop(self, val):
        return self.stacks[-1].pop()

    def popAt(self, idx):
        if idx >= len(self.stacks):
            raise IndexError
        return self.stacks[idx].pop()

