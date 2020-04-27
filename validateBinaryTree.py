class Solution:
    def validateBinaryTree(self, n, leftChild, rightChild):
        parentCount = [0]*n
        for i in range(n):
            if leftChild[i] != -1:
                parentCount[leftChild[i]] += 1
            if rightChild[i] != -1:
                parentCount[rightChild[i]] += 1
        print(parentCount)
        rootNo = 0
        rootIdx = 0
        for i, count in enumerate(parentCount):
            if count == 0:
                rootNo += 1
                rootIdx = i
            if count > 1 or rootNo > 1:
                return False
        if rootNo != 1:
            return False
        parentCount = [0]*n
        stack = [rootIdx]
        while len(stack) > 0:
            cur = stack.pop()
            if parentCount[cur] != 0:
                return False
            parentCount[cur] = 1
            if leftChild[cur] != -1:
                stack.append(parentCount[leftChild[cur]])
            if rightChild[cur] != -1:
                stack.append(parentCount[rightChild[cur]])
        if sum(parentCount) != n:
            return False
        else:
            return True



n = 4
leftChild = [1,2,0,-1]
rightChild = [-1,-1,-1,-1]
a = Solution()
print(a.validateBinaryTree(n, leftChild, rightChild))