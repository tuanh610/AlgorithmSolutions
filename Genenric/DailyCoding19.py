from random import randint

class Solution:
    def findLostCost(self, arr):

        def find2Low(input):
            lowest, lower, lowestIdx = float('inf'), float('inf'), -1
            for i in range(len(input)):
                if lowest >= input[i]:
                    lowestIdx = i
                    lower = lowest
                    lowest = input[i]
                elif lowest < input[i] < lower:
                    lower = input[i]
            return (lowest, lower, lowestIdx)

        lowest, lower, lowestIdx = find2Low(arr[-1])

        for i in range(len(arr)-2,-1,-1):
            for j in range(len(arr[i])):
                if j == lowestIdx:
                    arr[i][j] += lower
                else:
                    arr[i][j] += lowest
            print(arr[i])
            lowest, lower, lowestIdx = find2Low(arr[i])
        return lowest


if __name__ == '__main__':
    row = 5
    col = 5
    arr = []
    for _ in range(row):
        arr.append([randint(1,100) for _ in range(col)])
    for item in arr:
        print(item)
    print("============================")
    A = Solution()
    print(A.findLostCost(arr))