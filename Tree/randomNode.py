from random import randint
class Node:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
        self.nodeNumber = 1

    def __str__(self):
        return str(self.val)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, val, node=None):
        if self.root is None:
            self.root = Node(val)
            return
        if node is None:
            node = self.root
        if val == node.val:
            raise ValueError
        node.nodeNumber += 1
        if val < node.val:
            if node.left is None:
                node.left = Node(val)
                return
            else:
                self.insert(val, node.left)
        else:
            if node.right is None:
                node.right = Node(val)
                return
            else:
                self.insert(val, node.right)

    def contain(self, val, node=None):
        if self.root is None:
            return None
        if node is None:
            node = self.root
        if val == node.val:
            return node
        elif val < node.val:
            if node.left is None:
                return None
            else:
                return self.contain(val, node.left)
        else:
            if node.right is None:
                return None
            else:
                return self.contain(val, node.right)

    def getRandom(self, node=None):
        if node is None:
            node = self.root
        totalNode = node.nodeNumber
        choice = randint(1, totalNode)
        if choice == 1:
            return node
        if node.left is None or choice > 1 + node.left.nodeNumber:
            return self.getRandom(node.right)
        else:
            return self.getRandom(node.left)


    def BFSPrint(self):
        if self.root is None:
            return
        data = [self.root]
        end = self.root
        while len(data) > 0:
            node = data.pop(0)
            print(node)
            if node.left is not None:
                data.append(node.left)
            if node.right is not None:
                data.append(node.right)
            if node == end and len(data)>0:
                end = data[-1]
                print("================")

if __name__ == '__main__':
    a = BST()
    a.insert(10)
    a.insert(-1)
    a.insert(0)
    a.insert(12)
    a.insert(11)
    a.insert(5)
    a.insert(20)
    a.insert(17)
    data = {}
    for i in range(800):
        temp = a.getRandom().val
        data[temp] = data.get(temp, 0) + 1
    for key, val in data.items():
        print("{}: {} time".format(key, val))