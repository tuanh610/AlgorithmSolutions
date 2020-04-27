import LinkList.Generic as Generic

class Solution:
    def partition(self, n, head):
        if head is None:
            return head
        if head.val < n:
            partionPt = head
        else:
            partionPt = None
        curPt = head
        while curPt.next is not None:
            if curPt.next.val < n:
                if partionPt is None:
                    head, curPt.next = curPt.next, head
                    head.next, curPt.next.next = curPt.next.next, head.next
                    partionPt = head
                else:
                    partionPt.next, curPt.next = curPt.next, partionPt.next
                    partionPt.next.next, curPt.next.next = curPt.next.next, partionPt.next.next
                    partionPt = partionPt.next
            curPt = curPt.next
        return head
a = Solution()
b = Generic.GenerateLL(10)
Generic.printLL(b.head)
Generic.printLL(a.partition(5, b.head))
