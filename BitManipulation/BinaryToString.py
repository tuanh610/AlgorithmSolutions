#Convert number between 0 -> 1 to binary number
# example: ".101" = 1*(1/2^1) + 0*(1/2^2) + 1*(1/2^3)
#notice that "0.101" * 2 (base 10) = 1*(1/2^0) + 0*(1/2^1) + 1*(1/2^2) = "1.01"
#This means that for a certain number, if multiply by 2 give >1 results means that bit is 1, else 0
#stop when number turns to 0 (or exceed 32 chars)

class Solution:
    def BinaryToString(self, a):
        if a <= 0 or a >= 1:
            return "Error"
        res = "."
        while abs(a) > 10**-2:
            if len(res) > 32:
                return "Error"
            temp = a*2.0
            if temp >= 1:
                res += "1"
                a = temp-1.0
            else:
                res += "0"
                a = temp
        return res

if __name__ == "__main__":
    A = Solution()
    print(A.BinaryToString(0.625))
