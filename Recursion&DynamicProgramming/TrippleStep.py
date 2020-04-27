class Solution:
    def countPossibleWay(self, N):
        data = {1:1,2:2,3:4}

        def count(n):
            if n in data:
                return data[n]
            else:
                data[n] = count(n-1) + count(n-2) + count(n-3)
                return data[n]
        return count(N)


if __name__ == '__main__':
    N = 5
    A = Solution()
    print(A.countPossibleWay(N))