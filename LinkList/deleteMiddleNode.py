import LinkList.Generic as Generic

class Solution:
    def deleteMiddle(self, head):
        if head.next is None:
            return head
        elif head.next.next is None:
            return head.next

        fast = head
        slow = head
        while True:
            fast = fast.next.next
            if fast.next is not None and fast.next.next is not None:
                slow = slow.next
            else:
                break
        slow.next = slow.next.next
        return head

a = Solution()
b = Generic.GenerateLL(9)
Generic.printLL(b.head)
Generic.printLL(a.deleteMiddle(b.head))