import BitManipulation.Generic as Generic

class Solution:
    def pairwiseSwap(self, num):
        #Assume number is of type integer 32 bits
        onlyEven = 0xAAAAAAAA
        onlyOdd = 0x55555555
        #calculate even and odd bit number
        even = num & onlyEven
        odd = num & onlyOdd
        #shift right even + shiftleft odd
        even = even >> 1
        odd = odd << 1
        return even | odd

if __name__ == '__main__':
    bin = "110110101101100"
    print(" "+bin)
    num = Generic.BinaryStringToDec(bin)
    A = Solution()
    res = A.pairwiseSwap(num)
    print(Generic.DecToBinaryString(res))