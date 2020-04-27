from Tree.binarySearchTree import Node
class Solution:
    def weave(self, arr1, arr2, prefix=[]):
        if len(arr1) == 0:
            return [prefix + arr2]
        elif len(arr2) == 0:
            return [prefix + arr1]
        else:
            temp1 = self.weave(arr1[1:], arr2, prefix + [arr1[0]])
            temp2 = self.weave(arr1, arr2[1:], prefix + [arr2[0]])
            return temp1 + temp2

    def BSTSequence(self, head):
        if head.left is None and head.right is None:
            return [[head.val]]
        left = None
        right = None

        if head.left is not None:
            left = self.BSTSequence(head.left)
        if head.right is not None:
            right = self.BSTSequence(head.right)

        if left is None:
            return [[head.val]+x for x in right]
        elif right is None:
            return [[head.val]+x for x in left]
        else:
            temp = []
            for leftitem in left:
                for rightItem in right:
                    temp += self.weave(leftitem, rightItem)
            return [[head.val]+x for x in temp]

if __name__ == '__main__':
    node1 = Node(10)
    node2 = Node(5)
    node3 = Node(15)
    node4 = Node(2)
    node5 = Node(7)
    node6 = Node(12)
    node7 = Node(17)
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6
    node3.right = node7
    a = Solution()
    for item in a.BSTSequence(node1):
        print(item)

