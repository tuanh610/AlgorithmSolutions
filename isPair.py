class Solution:
    def isPair(self, arr, k):
        arr.sort()
        memo = {}
        return self.isPairRecursive(arr, k, memo)

    def isPairRecursive(self, arr, k, memo):
        def getKey(arr):
            return '-'.join([str(x) for x in arr])
        key = getKey(arr)
        if key in memo:
            return memo[key]

        if len(arr) == 2:
            if (arr[0] + arr[1]) % k == 0:
                return True
            else:
                return False

        for i in range(len(arr)-1):
            for j in range(i+1, len(arr)):
                if (arr[i] + arr[j]) % k == 0:
                    newArr = arr[:i] + arr[i+1:j]
                    if j < len(arr) - 1:
                        newArr += arr[j+1:]
                    if self.isPairRecursive(newArr, k, memo):
                        memo[key] = True
                        return True
        memo[key] = False
        return False

a = Solution()
b = [0,2,4,6,12,20,18,4]
print(a.isPair(b,4))





