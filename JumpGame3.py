from random import seed
from random import randint


class Node:
    def __init__(self, val):
        self.val = val
        self.neihbors = []
        self.visited = False


class Solution2:
    def buildGraph(self, arr):
        nodes = [Node(val) for val in arr]
        for i in range(len(arr)):
            if i - arr[i] >= 0:
                nodes[i].neihbors.append(nodes[i - arr[i]])
            if i + arr[i] < len(arr):
                nodes[i].neihbors.append(nodes[i + arr[i]])
        return nodes

    def canReach(self, arr, start) -> bool:
        nodes = self.buildGraph(arr)
        stack = [nodes[start]]
        while len(stack) > 0:
            node = stack.pop(len(stack) - 1)
            if node.val == 0:
                return True
            node.visited = True
            for neighbor in node.neihbors:
                if not neighbor.visited:
                    stack.append(neighbor)
        return False

class Solution:
    def jumpGame(self, arr, start):
        visited = [False]*len(arr)
        stack = [(arr[start],start)]
        while len(stack) > 0:
            val, idx = stack.pop(len(stack)-1)
            if val == 0:
                return True
            visited[idx] = True
            if idx-val >= 0 and not visited[idx-val]:
                stack.append((arr[idx-val], idx-val))
            if idx + val < len(arr) and not visited[idx + val]:
                stack.append((arr[idx + val], idx + val))

        return False

seed(3)
arr = [4,2,3,0,3,1,2]
#arr = [randint(0, 14) for _ in range(15)]
print(arr)
a = Solution()
print(a.jumpGame(arr, 0))
