#https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/

class Solution:
    def findCost(self, A):
        temp = [max(A[i],A[i+1]) for i in range(len(A)-1)]
        minItem = min(temp)
        minIdx = temp.index(minItem)
        if A[minIdx+1] < A[minIdx]:
            minIdx += 1
        minItem = A[minIdx]
        left = minIdx - 1
        right = minIdx + 1
        maxNode = minItem
        sum = 0
        while left >= 0 or right < len(A):
            if right >=len(A) or (left >= 0 and A[left]<A[right]):
                sum += maxNode*A[left]
                maxNode = max(maxNode, A[left])
                left -= 1
            else:
                sum += maxNode*A[right]
                maxNode = max(maxNode, A[right])
                right += 1

        return sum

a = Solution()
b = [3,7,2,12,15,10,3,9]
print(a.findCost(b))
