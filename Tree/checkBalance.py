class Node:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

    def __str__(self):
        return str(self.val)

class Solution:
    def checkBalance(self, head:Node):

        def dfs(node, curdepth):
            if node is None:
                return curdepth
            curdepth += 1
            if node.left is None and node.right is None:
                return curdepth
            leftDepth = dfs(node.left, curdepth)
            rightDepth = dfs(node.right, curdepth)
            if leftDepth == -1 or rightDepth == -1 or abs(leftDepth-rightDepth)>1:
                return -1
            else:
                return max(leftDepth, rightDepth)

        temp = dfs(head, 0)
        if temp != -1:
            return True
        else:
            return False

if __name__ == '__main__':
    nodes = [Node(x) for x in range(1,12)]
    nodes[0].left = nodes[1]
    nodes[0].right = nodes[2]
    nodes[1].left = nodes[3]
    nodes[1].right = nodes[4]
    nodes[2].left = nodes[5]
    nodes[2].right = nodes[6]
    nodes[4].left = nodes[7]
    nodes[5].right = nodes[8]
    nodes[8].left = nodes[9]
    nodes[6].right = nodes[10]

    a = Solution()
    print(a.checkBalance(nodes[0]))



