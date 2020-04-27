class Node:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

    def __str__(self):
        return str(self.val)


class Solution:
    def firstCommonAncestor(self, head, node1, node2):

        def consist(head, target):
            stack = [head]
            while len(stack) > 0:
                cur = stack.pop()
                if cur == target:
                    return True
                if cur.left is not None:
                    stack.append(cur.left)
                if cur.right is not None:
                    stack.append(cur.right)
            return False

        def dfs(node):
            if node is None:
                return None
            if node == node1 or node == node2:
                return node

            left = dfs(node.left)
            right = dfs(node.right)

            if left is None and right is None:
                return None
            elif left is None:
                return right
            elif right is None:
                return left
            else:
                return node

        #first check if either is the parent of the other
        if consist(node1, node2):
            return node1
        elif consist(node2, node1):
            return node2
        else:
            temp = dfs(head)
            if temp != node1 and temp != node2:
                return temp
            else:
                return None

if __name__ == '__main__':
    nodes = [Node(x) for x in range(1,13)]
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
    A = Solution()
    print(A.firstCommonAncestor(nodes[0], nodes[10], nodes[11]))