class Solution:
    def printsteps1(self, n):
        for i in range(1,n+1):
            print("#"*i + '_'*(n-i))

    def printstepsRecursive(self, n, row=0, stair=''):
        if n == row:
            return
        if n == len(stair):
            print(stair)
            self.printstepsRecursive(n, row+1)
            return
        if len(stair) <= row:
            stair += '#'
        else:
            stair += '_'
        self.printstepsRecursive(n, row, stair)

a = Solution()
a.printstepsRecursive(5)