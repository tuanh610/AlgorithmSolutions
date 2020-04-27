# 3, 4, 5, -9, 5
class Solution:
    def sumSubArrToZero(self, arr):
        sums = {}
        curSum = 0
        temparr = [0] + arr
        for i, item in enumerate(temparr):
            curSum += temparr[i]
            if curSum in sums:
                sums[curSum].append(i)
            else:
                sums[curSum] = [i]
        res = []
        for key, val in sums.items():
            if len(val) > 1:
                for i in range(len(val)-1):
                    res.append(temparr[(val[i]+1):(val[i+1]+1)])
        return res

a = Solution()
b = [3, 4 , -7, 3, 1, 3, 1, -4, -2, -2]
print(a.sumSubArrToZero(b))