from Tree.buildBinaryTree import Node

class LLNode:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __str__(self):
        return str(self.val)

class Solution():
    def listOfDepth(self, head):
        curlvl = -1
        queue = [(head,0)]
        res = []
        while len(queue) > 0:
            node, lvl = queue.pop(0)
            if curlvl != lvl:
                res.append(LLNode(node))
                curlvl = lvl
            else:
                curLL = res[-1]
                while curLL.next is not None:
                    curLL = curLL.next
                curLL.next = LLNode(node)
            if node.left is not None:
                queue.append((node.left, lvl+1))
            if node.right is not None:
                queue.append((node.right, lvl+1))
        return res

if __name__ == '__main__':
    nodes = [Node(x) for x in range(1,8)]
    nodes[0].left = nodes[1]
    nodes[0].right = nodes[2]
    nodes[1].left = nodes[3]
    nodes[1].right = nodes[4]
    nodes[2].left = nodes[5]
    nodes[2].right = nodes[6]

    a = Solution()
    res = a.listOfDepth(nodes[0])
    print("Done")