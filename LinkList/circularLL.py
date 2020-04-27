import LinkList.Generic as Generic

class Solution:
    def circularLL(self, head):
        visited = set()
        cur = head
        while cur is not None:
            if cur in visited:
                return cur
            visited.add(cur)
            cur = cur.next
        return None

    def circularLLNoHash(self, head):
        slow, fast = head, head
        colidePoint = None
        while slow is not None and head is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                colidePoint = slow
                break
        if colidePoint is None:
            return None
        else:
            first = head
            second = colidePoint
            while first is not None and second is not None:
                if first == second:
                    return first
                first = first.next
                second = second.next
            return  None

a = Solution()
nodes = [Generic.Node(1), Generic.Node(2), Generic.Node(3), Generic.Node(4), Generic.Node(5), Generic.Node(6), Generic.Node(7)]
for i in range(6):
    nodes[i].next = nodes[i+1]
nodes[6].next = nodes[3]

print(a.circularLLNoHash(nodes[0]))