class Solution:
    def findMaxNonAdjSum(self, arr):
        maxVal = 0
        for i in range(2, len(arr)):
            if maxVal < arr[i-2]:
                maxVal = arr[i-2]
            arr[i] += max(maxVal,0)
        return max(arr)


if __name__ == '__main__':
    arr = [5,1, -1, 5, 3, 2, 6, 1, 6]
    A = Solution()
    print(A.findMaxNonAdjSum(arr))