from stackImplimentation import LinklistStack

class Solution:
    def sortStack(self, top:LinklistStack):
        temp = LinklistStack()
        res = LinklistStack()
        while not top.isEmpty():
            cur = top.pop()
            if res.isEmpty() or res.peek() < cur:
                res.push(cur)
            else:
                while not res.isEmpty() and res.peek() > cur:
                    temp.push(res.pop())
                res.push(cur)
            if top.isEmpty() and not temp.isEmpty():
                top = temp
                temp = LinklistStack()
        return res

a = Solution()
b = LinklistStack()
b.push(5)
b.push(8)
b.push(6)
b.push(2)
b.push(4)
c = a.sortStack(b)
while not c.isEmpty():
    print(c.pop())

