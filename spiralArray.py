class Solution:
    def spiralArray(self, n):
        val = 1
        res = [[0 for _ in range(n)] for _ in range(n)]
        startR, startC, endR, endC = 0, 0, n-1, n-1
        while startR <= endR and startC <= endC:
            #top
            for c in range(startC, endC+1):
                #print(startR, c)
                res[startR][c] = val
                val+=1
            startR += 1
            #right
            for r in range(startR, endR+1):
                #print(r, endC)
                res[r][endC] = val
                val += 1
            endC -= 1
            #bot
            for c in range(endC, startC-1, -1):
                #print(endR, c)
                res[endR][c] = val
                val += 1
            endR -= 1
            #right
            for r in range(endR, startR-1, -1):
                #print(r, startC)
                res[r][startC] = val
                val += 1
            startC += 1
        return res

a = Solution()
res = a.spiralArray(6)
for item in res:
    print(item)
