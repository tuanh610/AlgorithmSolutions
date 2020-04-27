class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __str__(self):
        return str(self.val)

class Solution:
    def nFromlast(self, n, head):
        if head is None:
            return None
        target = head
        cur = head
        for i in range(n):
            cur = cur.next
            if cur is None:
                return None
        while cur.next is not None:
            cur = cur.next
            target = target.next
        return target

a = Solution()
node1 = Node(5)
node2 = Node(10)
node3 = Node(15)
node4 = Node(20)
node5 = Node(25)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print(a.nFromlast(0, node1))