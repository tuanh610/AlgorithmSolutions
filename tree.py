class Node:
    def __init__(self, val):
        self.val = val
        self.children = []

    def addChild(self, val):

        self.children.append(Node(val))

    def removeChild(self, val):
        for child in self.children:
            if child.val == val:
                self.children.remove(child)
                break

class Tree:
    def __init__(self):
        self.root = None

    def transverseDFS(self, node=None):
        if self.root is None:
            return
        elif node is None:
            node = self.root
        print(node.val)
        for child in node.children:
            self.transverseDFS(child)

    def transverseBFS(self):
        if self.root is None:
            return
        q = [self.root]
        while len(q) > 0:
            node = q.pop(0)
            print(node.val)
            q += node.children

class Solution:
    def levelWidth(self, root):
        if root is None:
            return []
        res = [1]
        q = [root]
        end = root
        while len(q) > 0:
            node = q.pop(0)
            q += node.children
            if node == end and len(q) > 0:
                res.append(len(q))
                end = q[-1]
        return res
 
node1 = Node(5)
node2 = Node(10)
node3 = Node(15)
node4 = Node(20)
node5 = Node(25)
node6 = Node(30)
node7 = Node(35)
node8 = Node(40)
node9 = Node(45)
node1.children = [node2, node3, node4]
node2.children = [node5, node6]
node3.children = [node7, node8]
node5.children = [node9]
#a = Tree()
#a.root = node1
b = Solution()
print(b.levelWidth(node1))


