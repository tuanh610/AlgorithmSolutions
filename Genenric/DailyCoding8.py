class Node:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
        self.parent = None

    def __str__(self):
        return str(self.val)

class Solution:
    def countUnivalTree(self, head):
        def count(node):
            if node is None:
                return (True, 0)
            elif node.left is None and node.right is None:
                return (True,1)
            leftUnival, leftCount = count(node.left)
            rightUnival, rightCount = count(node.right)
            totalCount = leftCount + rightCount
            if leftUnival and rightUnival and (node.left is None or node.val == node.left.val) and (node.right is None or node.val == node.right.val):
                return (True, totalCount+1)
            else:
                return (False, totalCount)
        _, res = count(head)
        return res

if __name__ == "__main__":
    a = Solution()
    #nodes = [Node('a'), Node('a'), Node('a'), Node('a'), Node('a'), Node('A')]
    nodes = [Node('a'), Node('c'), Node('b'), Node('b'), Node('b'), Node('b')]
    nodes[0].left = nodes[1]
    nodes[0].right = nodes[2]
    nodes[2].left = nodes[3]
    nodes[2].right = nodes[4]
    nodes[4].right = nodes[5]
    print(a.countUnivalTree(nodes[0]))