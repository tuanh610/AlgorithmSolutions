from random import choice
class Solution:
    def powerSet(self, input):
        listinput = list(input)

        def getList(arr):
            if len(arr) == 0:
                raise ValueError
            elif len(arr) == 1:
                return [arr, []]
            temp = getList(arr[1:])
            return temp + [[arr[0]]+x for x in temp]

        return getList(listinput)

if __name__ == '__main__':
    A = Solution()
    input = {"a", "i", "o"}
    print(A.powerSet(input))
