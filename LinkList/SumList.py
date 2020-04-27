import LinkList.Generic as Generic

class Solution:
    def sumList(self, head1, head2):

        def makeSameLength(head1, head2):
            l1, l2 = 0, 0
            cur1, cur2 = head1, head2
            while cur1 is not None or cur2 is not None:
                if cur1 is not None:
                    l1 += 1
                    cur1 = cur1.next
                if cur2 is not None:
                    l2 += 1
                    cur2 = cur2.next
            if l1 > l2:
                for _ in range(l1-l2):
                    temp = Generic.Node(0)
                    temp.next = head2
                    head2 = temp
            elif l2 > l1:
                for _ in range(l2-l1):
                    temp = Generic.Node(0)
                    temp.next = head1
                    head1 = temp
            return head1, head2

        def addSameLength(head1, head2):
            if head1 is None and head2 is None:
                return (0, 0, 0)
            else:
                right, order, carry = addSameLength(head1.next, head2.next)
                left = head1.val + head2.val + carry
                newcarry = 0
                if left > 9:
                    left -= 10
                    newcarry = 1
                return (left * (10 ** order) + right, order + 1, newcarry)

        newHead1, newHead2 = makeSameLength(head1, head2)
        Generic.printLL(newHead1)
        Generic.printLL(newHead2)
        res, _, _ = addSameLength(newHead1, newHead2)
        return res

a = Solution()
ll1 = Generic.GenerateLL(2)
ll2 = Generic.GenerateLL(5)
Generic.printLL(ll1.head)
Generic.printLL(ll2.head)
print(a.sumList(ll1.head, ll2.head))