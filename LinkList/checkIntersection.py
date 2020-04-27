import LinkList.Generic as Generic

class Solution:
    def checkIntersection(self, h1, h2):
        if h1 is None or h2 is None:
            return None
        l1, l2 = 0, 0
        cur1, cur2 = h1, h2
        while cur1 is not None or cur2 is not None:
            if cur1 is not None:
                l1 += 1
                cur1 = cur1.next
            if cur2 is not None:
                l2 += 1
                cur2 = cur2.next
        cur1, cur2 = h1, h2
        if l1 > l2:
            for _ in range(l1-l2):
                cur1 = cur1.next
        elif l2 > l2:
            for _ in range(l2-l1):
                cur2 = cur2.next
        while cur1 is not None and cur2 is not None:
             if cur1 == cur2:
                 return cur1
             cur1 = cur1.next
             cur2 = cur2.next
        return None

a = Solution()
nodes = [Generic.Node(1), Generic.Node(2), Generic.Node(3), Generic.Node(4), Generic.Node(5), Generic.Node(6), Generic.Node(7)]
for i in range(4):
    nodes[i].next = nodes[i+1]
nodes[6].next = nodes[5]

temp = a.checkIntersection(nodes[0], nodes[6])
print(temp)