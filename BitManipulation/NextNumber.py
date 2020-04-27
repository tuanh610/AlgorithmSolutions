import BitManipulation.Generic as Generic

class Solution:
    def getNextBiggerNumber(self, num):
        #first find the non trailing 0
        oneCounter = 0
        pivot = -1
        bitCounter = -1
        foundOne = False
        curNum = num
        while curNum > 0:
            bitCounter += 1
            if curNum % 2 == 0:
                if foundOne:
                    pivot = bitCounter
                    break
            else:
                oneCounter += 1
                foundOne = True
            curNum = curNum // 2
        if pivot == -1:
            return None
        #now we need to:
        #set the bit at pivot, reset all the trailing 0, add back oneCounter-1 "1"
        temp = Generic.setBit(num, pivot)
        #print(Generic.DecToBinaryString(temp))
        temp = Generic.clearBitFromStart(temp, pivot-1)
        #print(Generic.DecToBinaryString(temp))
        setNum = (1 << oneCounter-1) - 1
        #print(Generic.DecToBinaryString(setNum))
        temp = temp | setNum
        #print(Generic.DecToBinaryString(temp))
        return temp

    def getPrevSmallerNumber(self, num):
        #first find the non trailing 1
        oneCounter = 0
        pivot = -1
        bitCounter = -1
        foundZero = False
        curNum = num
        while curNum > 0:
            bitCounter += 1
            if curNum % 2 == 0:
                foundZero = True
            else:
                if foundZero:
                    pivot = bitCounter
                    break
                else:
                    oneCounter += 1
            curNum = curNum // 2
        if pivot == -1:
            return None
        #now we need to:
        #reset the bit at pivot till start, add back oneCounter+1 "1"
        temp = Generic.clearBitFromStart(num, pivot)
        print(Generic.DecToBinaryString(temp))
        setNum = (1 << oneCounter+1) - 1
        print(Generic.DecToBinaryString(setNum))
        temp = temp | setNum
        print(Generic.DecToBinaryString(temp))
        return temp

if __name__ == '__main__':
    A = Solution()
    binNum = "11011001111011"
    num = Generic.BinaryStringToDec(binNum)
    print(num)
    print(A.getPrevSmallerNumber(num))
