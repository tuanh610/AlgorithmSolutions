class Solution:
    def chunk(self, arr, n):
        res = []
        idx = 0
        while idx < len(arr):
            end = min(len(arr), idx+n)
            res.append(arr[idx:end])
            idx = end
        return res

a = Solution()
print(a.chunk([], 10))
print(a.chunk([1,2,3,4,5,6,7,8],2))