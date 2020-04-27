import LinkList.Generic as Generic

class Solution:
    def removeDupWithSpace(self, head):
        if head is None:
            return head
        data = set()
        data.add(head.val)
        cur = head
        while cur is not None and cur.next is not None:
            if cur.next.val in data:
                cur.next = cur.next.next
            else:
                data.add(cur.next.val)
                cur = cur.next
        return head

    def removeDupWithoutBuffer(self, head):
        if head is None:
            return head
        cur = head
        while cur is not None:
            nxt = cur
            while nxt is not None and nxt.next is not None:
                if cur.val == nxt.next.val:
                    nxt.next = nxt.next.next
                else:
                    nxt = nxt.next
            cur = cur.next
        return head

a = Solution()
b = Generic.GenerateLL(100)
Generic.printLL(b.head)
Generic.printLL(a.removeDupWithoutBuffer(b.head))
