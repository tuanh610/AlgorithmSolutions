class Solution:
    def missingInteger(self, arr):
        #first move all non positive number to the left
        pos = 0
        while arr[pos] <= 0 and pos < len(arr):
            pos += 1
        cur = pos + 1
        while cur < len(arr):
            if arr[cur] <= 0:
                arr[pos], arr[cur] = arr[cur], arr[pos]
                pos += 1
            cur += 1
        for i in range(pos, len(arr)):
            val = abs(arr[i])+pos-1
            if val < len(arr):
                arr[val] = -arr[val]
        for i in range(pos, len(arr)):
            if arr[i] > 0:
                return i - pos + 1
        return len(arr)-pos + 1

a = Solution()
arr = [-1, 5, 3, 1, 0, 4, 2]
print(a.missingInteger(arr))