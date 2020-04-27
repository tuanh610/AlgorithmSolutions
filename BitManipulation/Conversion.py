#Find number of bit needed to be flipped to turn a -> b
import BitManipulation.Generic as Generic

class Solution:
    def conversion(self,a ,b):
        res = 0
        while a > 0 and b > 0:
            if a%2 != b%2:
                res += 1
            a = a//2
            b = b//2
        while a>0:
            if a%2 == 1:
                res += 1
            a = a//2
        while b > 0:
            if b%2 == 1:
                res += 1
            b = b//2
        return  res

if __name__ == '__main__':
    a = 100
    b = 15
    print(Generic.DecToBinaryString(a))
    print(Generic.DecToBinaryString(b))
    A = Solution()
    print(A.conversion(b,a))  