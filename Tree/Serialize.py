class Node:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

    def __str__(self):
        return str(self.val)

class Solution:
    def serialize(self, root):
        res = ""
        stack = [root]
        while len(stack)>0:
            curNode = stack.pop()
            if curNode is None:
                res += "N|"
            else:
                res += str(curNode.val) + "|"
                stack.append(curNode.right)
                stack.append(curNode.left)
        return res

    def deserialize(self, A:str):
        data = A.split('|')
        def convert(idx):
            #print(A[idx], idx)
            if data[idx] == "N":
                return (None, idx)
            curNode = Node(int(data[idx]))
            curNode.left, idx = convert(idx+1)
            curNode.right, idx = convert(idx+1)
            return (curNode, idx)

        res, lastIdx = convert(0)
        return res

A = Solution()
nodes = [Node(1), Node(2), Node(3), Node(4), Node(5), Node(6), Node(7), Node(8), Node(9), Node(10)]
nodes[0].left = nodes[1]
nodes[0].right = nodes[6]
nodes[1].left = nodes[3]
nodes[1].right = nodes[4]
nodes[3].right = nodes[7]
nodes[6].right = nodes[2]
nodes[2].right = nodes[5]
nodes[5].left = nodes[9]
nodes[5].right = nodes[8]

ser = A.serialize(nodes[0])
print(ser)
res = A.deserialize(ser)
print(res)