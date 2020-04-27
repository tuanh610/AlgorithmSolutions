class Solution:
    def reverseInt(self, a:int):
        neg = True if a < 0 else False
        a = abs(a)
        res = 0
        counter = 0
        while a > 0:
            res = res*10+a%10
            counter += 1
            a = a//10
        return res if not neg else -res

    def reverseInt2(self, a:int):
        start = 0 if a >= 0 else 1
        temp = str(a)[start:]
        temp = int("".join(temp[::-1]))
        return temp if start == 0 else -temp

a = Solution()
print(a.reverseInt2(1914))

