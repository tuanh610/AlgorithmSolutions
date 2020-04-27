class Solution:
    def iterativePrint(self, n):
        totalSize = 2*n - 1
        for i in range(1,n+1):
            totalslot = 2*i-1
            side = (totalSize - totalslot) // 2
            print('_'*side + "#"*totalslot + "_"*side)

    def recursivePrint(self, n, row=0, piramid=''):
        if row == n:
            return
        if len(piramid) == 2*n-1:
            print(piramid)
            self.recursivePrint(n, row+1)
            return
        if len(piramid) < n-row-1 or len(piramid) > n+row-1:
            piramid += '_'
        else:
            piramid += "#"
        self.recursivePrint(n, row, piramid)

a = Solution()
a.recursivePrint(10)