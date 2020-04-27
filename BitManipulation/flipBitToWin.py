import BitManipulation.Generic as Generic
class Solution:
    def flipBit(self, num):
        data = {}
        oneCounter = 0
        prevIdx = -1
        curBit = -1
        while num > 0:
            curBit += 1
            temp = num % 2
            if temp == 0:
                data[curBit] = oneCounter + 1
                if prevIdx in data:
                    data[prevIdx] += oneCounter
                prevIdx = curBit
                oneCounter = 0
            else:
                oneCounter += 1
            num = num // 2
        if prevIdx in data:
            data[prevIdx] += oneCounter

        return max(data.values())

if __name__ == "__main__":
    bin = "11011100111"
    num = 1775
    A = Solution()
    print(A.flipBit(Generic.BinaryStringToDec(bin)))
