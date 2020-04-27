class Solution:
    def climbStair(self, N):
        data = {1:1, 2:2}
        def climb(n):
            if n in data:
                return data[n]
            else:
                temp = climb(n-1) + climb(n-2)
                data[n] = temp
                return temp
        return climb(N)

if __name__ == '__main__':
    A = Solution()
    print(A.climbStair(3))

