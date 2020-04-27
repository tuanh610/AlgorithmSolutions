class Solution:
    def getKey(self, arr):
        return '-'.join([str(x) for x in arr])

    def partition(self, arr, K, mem={}):
        key = self.getKey(arr)
        if key in mem:
            return mem[key]
        #Base case
        if len(arr) <= K:
            return max(arr)*len(arr)
        #Create choices
        maxVal = -float('inf')
        maxSum = -float('inf')
        for i in range(0,min(K,len(arr)-1)):
            maxVal = max(arr[i], maxVal)

            leftVal = maxVal * (i + 1)
            newArr = arr[i + 1:]
            rightVal = self.partition(newArr, K, mem)
            tempSum = maxVal * (i + 1) + rightVal
            #Debug print
            print(arr[:i+1])
            print(arr[i+1:])
            print("left: {}".format(leftVal))
            print("right: {}".format(rightVal))
            maxSum = max(maxSum, tempSum)
        mem[key] = maxSum

        return maxSum

    def partition2(self, arr, K):
        res = [0]*len(arr)
        res[0] = arr[0]
        for n in range(1, len(arr)):
            maxVal = -float('inf')
            start = max(n-K+1, 0)
            for i in range(start,n+1):
                if i == n:
                    tempVal = max(arr[start:n+1])*(n+1-start)
                    if start != 0:
                        tempVal += res[start-1]
                else:
                    tempVal = res[i] + max(arr[i+1:n+1])*(n-i)
                maxVal = max(maxVal, tempVal)
            res[n] = maxVal
        return res[-1]

a = Solution()
b = [1,15,7,9,2,5,10]
print(a.partition2(b, 3))