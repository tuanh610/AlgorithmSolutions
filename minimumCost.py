#https://leetcode.com/problems/minimum-cost-for-tickets/
from functools import lru_cache

class Solution:
    def minimumCost(self, days, costs):
        N = len(days)

        duration = [1,7,30]

        @lru_cache(None)
        def dp(i):
            if i >= N:
                return 0
            j = i
            res = float('inf')
            for cost, day in zip(costs, duration):
                while j < N and days[j] < days[i] + day:
                    j+=1
                    res = min(res, dp(j)+cost)
            return res

        return dp(0)

a = Solution()
days = [1,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,20,21,24,25,27,28,29,30,31,34,37,38,39,41,43,44,45,47,48,49,54,57,60,62,63,66,69,70,72,74,76,78,80,81,82,83,84,85,88,89,91,93,94,97,99]
costs = [9,38,134]
print(a.minimumCost(days,costs))


