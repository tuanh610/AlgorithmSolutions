class Solution:
    def findMinRoom(self, times):
        start = sorted([x for x, _ in times])
        end = sorted(([x for _,x in times]))
        res, cur = 0, 0
        startIdx = 0
        endIdx = 0
        while startIdx < len(start) and endIdx < len(end):
            if start[startIdx] < end[endIdx]:
                cur += 1
                startIdx += 1
            else:
                cur -= 1
                endIdx += 1
            res = max(res, cur)
        return res


if __name__ == '__main__':
    times = [(30,75), (0, 50), (60, 150)]
    A = Solution()
    print(A.findMinRoom(times))