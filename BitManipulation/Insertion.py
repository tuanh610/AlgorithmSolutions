import BitManipulation.Generic as Generic

class Solution:
    def insertion(self, a, b, i, j):
        if len(b) > j-i+1:
            raise IndexError
        #Create mask of 0 from j -> i, rest should be 1 -> ~ (1 from i-j)
        numA = Generic.BinaryStringToDec(a)
        numB = Generic.BinaryStringToDec(b)
        #Clear bit j->i of num A
        mask = ~(Generic.clearBitFromStart(((1 << j+1)-1), i-1))
        numA = numA & mask
        #shit left num b i bit
        numB = numB << i
        return Generic.DecToBinaryString(numA | numB)

a = "10000000000"
b = "10011"
i = 1
j = 6
A = Solution()
print(A.insertion(a, b, i, j))