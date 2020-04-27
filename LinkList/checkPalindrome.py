import LinkList.Generic as Generic

class Solution:
    def reverseLL(self, cur, prev):
        if cur.next is None:
            self.head = cur
            cur.next = prev
            return

        next = cur.next
        cur.next = prev
        self.reverseLL(next, cur)

    def isPalindrome(self, head):
        l = 0
        cur = head
        while cur is not None:
            l += 1
            cur = cur.next
        midPoint = l//2

        def checkPalin(node, count):
            if count == midPoint:
                if l % 2 == 0:
                    check = node.next
                else:
                    check = node.next.next
                if check.val == node.val:
                    return (True, check.next)
                else:
                    return (False, None)
            inner, check = checkPalin(node.next, count+1)
            if inner and check.val == node.val:
                return (True, check.next)
            else:
                return (False, None)

        res, _ = checkPalin(head, 1)
        return res

a = Solution()
nodes = [Generic.Node(1), Generic.Node(2), Generic.Node(4), Generic.Node(2), Generic.Node(1) ]
for i in range(len(nodes)-1):
    nodes[i].next = nodes[i+1]
Generic.printLL(nodes[0])
print(a.isPalindrome(nodes[0]))