#https://leetcode.com/problems/find-eventual-safe-states/
class Solution:
    def eventualSafeNodes(self, graph):
        ignored = set()
        def dfs(curNode, visited):
            if visited[curNode]:
                ignored.add(curNode)
                return -1
            visited[curNode] = True
            if len(graph[curNode]) == 0:
                visited[curNode] = False
                return 0
            for newNode in graph[curNode]:
                #if newNode not in ignored:
                temp = dfs(newNode, visited)
                if temp == -1:
                    ignored.add(curNode)
                    visited[curNode] = False
                    return -1
            visited[curNode] = False
            return 0

        for i in range(len(graph)):
            if i not in ignored:
                visited = [False]*len(graph)
                dfs(i, visited)
        res = []
        for i in range(len(graph)):
            if i not in ignored:
                res.append(i)
        return res

graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]]
a = Solution()
print(a.eventualSafeNodes(graph))

