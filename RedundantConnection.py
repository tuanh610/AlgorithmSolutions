#https://leetcode.com/problems/redundant-connection/
class Solution:
    def redundantConnection(self, arr):
        data = {}
        for (a,b) in arr:
            if a not in data:
                data[a] = [b]
            else:
                data[a].append(b)
            if b not in data:
                data[b] = [a]
            else:
                data[b].append(a)
        visited = [False] * len(data)
        def dfs(curNode, ignore):
            if visited[curNode-1]:
                return [curNode]
            visited[curNode-1] = True
            for neighbor in data[curNode]:
                if neighbor != ignore:
                    temp = dfs(neighbor, curNode)
                    if len(temp) == 0:
                        continue
                    if temp[-1] == -1:
                        return temp
                    if temp[-1] == curNode:
                        return temp + [-1]
                    else:
                        return [curNode] + temp
            visited[curNode - 1] = False
            return []
        routes = dfs(1, -1)
        routes[-1] = routes[0]

        loops = set()
        for i in range(len(routes)-1):
            minVal = min(routes[i], routes[i+1])
            maxVal = max(routes[i], routes[i+1])
            loops.add((minVal, maxVal))
        for i in range(len(arr)-1,-1,-1):
            if (arr[i][0],arr[i][1]) in loops:
                return arr[i]
        return -1
    

path = [[2,7],[7,8],[3,6],[2,5],[6,8],[4,8],[2,8],[1,8],[7,10],[3,9]]
a = Solution()
print(a.redundantConnection(path))


