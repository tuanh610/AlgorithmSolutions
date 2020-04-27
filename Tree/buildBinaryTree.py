class Node:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

    def __str__(self):
        return str(self.val)

    def printDetail(self):
        print("Node: {}. Left: {}. Right: {}".format(self.val,
                                                      "None" if self.left is None else str(self.left.val),
                                                      "None" if self.right is None else str(self.right.val)))

class Solution:
    def buidBinaryTree(self, arr):
        def build(startIdx, endIdx):
            if startIdx > endIdx:
                return None
            mid = (endIdx - startIdx)//2 + startIdx
            node = Node(arr[mid])
            node.left = build(startIdx, mid-1)
            node.right = build(mid+1, endIdx)
            return node

        return build(0, len(arr)-1)

if __name__ == '__main__':
    arr = [x for x in range(1,10)]
    a = Solution()
    temp = a.buidBinaryTree(arr)
    queue = [temp]
    while len(queue) > 0:
        cur = queue.pop(0)
        cur.printDetail()
        if cur.left is not None:
            queue.append(cur.left)
        if cur.right is not None:
            queue.append(cur.right)

