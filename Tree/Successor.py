from Tree.binarySearchTree import Node
from Tree.binarySearchTree import BinarySearchTree

class Solution:
    def successor(self, node):
        #If has right branch
        if node.right is not None:
            cur = node.right
            while cur.left is not None:
                cur = cur.left
            return cur
        else:
            child = node
            parent = node.parent
            while parent is not None:
                if child.val < parent.val:
                    return parent
                else:
                    child = child.parent
                    parent = parent.parent
            return None

if __name__ == '__main__':
    tree = BinarySearchTree()
    tree.insert(5)
    tree.insert(10)
    tree.insert(3)
    tree.insert(6)
    tree.insert(11)
    tree.insert(8)
    stack = [tree.root]
    while len(stack) > 0:
        cur = stack.pop()
        if cur.left is not None:
            cur.left.parent = cur
            stack.append(cur.left)
        if cur.right is not None:
            cur.right.parent = cur
            stack.append(cur.right)
    A = Solution()
    res = A.successor(tree.root.right.right)
    print(res)
    print("Done")
