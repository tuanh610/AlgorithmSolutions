class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def isCircular(self, head):
        if head is None:
            return False
        slow = head
        fast = head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

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
node5.next = node3
print(a.isCircular(node1))