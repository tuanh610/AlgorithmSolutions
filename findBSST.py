class Node:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

    def __str__(self):
        return str(self.val)

class Solution:
    def findBST(self, head):
        node, height = self.findBSTRecursive(head)
        if height > 1:
            return node
        else:
            return None

    def findBSTRecursive(self, node):
        if node.left is None and node.right is None:
            return (node, 1)
        maxdepth = 0
        bstNode = None
        leftOk = True
        rightOk = True
        if node.left is not None:
            bstNode, maxdepth = self.findBSTRecursive(node.left)
            if bstNode != node.left or node.val <= bstNode.val:
                leftOk = False
        if node.right is not None:
            tempNode, tempdepth = self.findBSTRecursive(node.right)
            if tempNode != node.right or node.val >= tempNode.val:
                rightOk = False
            if tempdepth > maxdepth:
                maxdepth = tempdepth
                bstNode = tempNode
        if leftOk and rightOk:
            return (node, maxdepth+1)
        else:
            return (bstNode, maxdepth)

nodes = [Node(13), Node(11), Node(12), Node(15), Node(5), Node(30),
         Node(3), Node(7), Node(35), Node(1), Node(6), Node(10),
         Node(32)]

nodes[0].left = nodes[1]
nodes[0].right = nodes[2]
nodes[1].left = nodes[3]
nodes[3].left = nodes[4]
nodes[3].right = nodes[5]
nodes[4].left = nodes[6]
nodes[4].right = nodes[7]
nodes[5].right = nodes[8]
nodes[6].left = nodes[9]
nodes[7].left = nodes[10]
nodes[7].right = nodes[11]
nodes[8].left = nodes[12]

a = Solution()
print(a.findBST(nodes[0]))