class Node:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
        self.parent = None

    def __str__(self):
        return str(self.val)

class BinarySearchTree:
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
        elif val < node.val:
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

def validateBST(node, maxLim=float('inf'), minLim=-float('inf')):
    if minLim >= node.val or maxLim <= node.val:
        return False
    if node.left is None and node.right is None:
        return True
    if node.left is not None and not validateBST(node.left, node.val, minLim):
        return False
    if node.right is not None and not validateBST(node.right, maxLim, node.val):
        return False
    return True



# a = BinarySearchTree()
# a.insert(10)
# a.insert(-1)
# a.insert(0)
# a.insert(12)
# a.insert(11)
# a.insert(5)
# a.insert(20)
# a.insert(17)
# print(a.contain(21))
if __name__ == '__main__':
    node1 = Node(10)
    node2 = Node(0)
    node3 = Node(12)
    node4 = Node(-1)
    node5 = Node(5)
    node6 = Node(11)
    node7 = Node(20)
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6
    node3.right = node7
    print(validateBST(node1))


