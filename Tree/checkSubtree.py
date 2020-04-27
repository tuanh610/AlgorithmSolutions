from Tree.binarySearchTree import Node

class Solution:
    def checkSubTree(self, head1, head2):

        def getPreOrderString(node):
            if node is None:
                return "N"
            res = str(node.val)
            res += getPreOrderString(node.left)
            res += getPreOrderString(node.right)
            return res
        str1 = getPreOrderString(head1)
        str2 = getPreOrderString(head2)
        if str2 in str1:
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

    otherNodes = [Node(3), Node(6), Node(7), Node(9), Node(10), Node(11)]
    otherNodes[0].left = otherNodes[1]
    otherNodes[0].right = otherNodes[2]
    otherNodes[1].right = otherNodes[3]
    otherNodes[3].left = otherNodes[4]
    otherNodes[2].right = otherNodes[5]

    a = Solution()
    print(a.checkSubTree(nodes[0], otherNodes[0]))