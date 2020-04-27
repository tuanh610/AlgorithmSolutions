class Solution:
    def subSet(self, arr):
        res = [[], [arr[-1]]]
        for i in range(len(arr)-2, -1, -1):
            for j in range(len(res)):
                res.append([arr[i]]+res[j])
        return res

a = Solution()
b = a.subSet([1,2,3,4])
for item in b:
    print(item)