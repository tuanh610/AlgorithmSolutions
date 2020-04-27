class Solution:
    def fibonacci(self, n, data={}):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n in data:
            return data[n]
        temp = self.fibonacci(n-1) + self.fibonacci(n-2)
        data[n] = temp
        return temp

a = Solution()
print(a.fibonacci(120))