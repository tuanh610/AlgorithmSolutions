from _collections import defaultdict

class Solution:
    def evaluateDivision(self, equations, values, queries):
        #build the grapth
        data = defaultdict(list)
        for i, (start, end) in enumerate(equations):
            ratio = values[i]
            data[start].append((end,ratio))
            data[end].append((start, 1/ratio))
        #print(data)

        def dfs(nodeVal, cost, target, visited):
            if nodeVal == target:
                return cost
            visited.add(nodeVal)
            for newnode, newcost in data[nodeVal]:
                if newnode not in visited:
                    temp = dfs(newnode, newcost, target, visited)
                    if temp != -1:
                        return cost*temp
            return -1

        res = []
        for (valS, valE) in queries:
            if valS in data:
                visited = set()
                res.append(dfs(valS, 1, valE, visited))
            else:
                res.append(-1)
        return res


equations = [ ["a", "b"], ["b", "c"] ]
values = [2.0, 3.0]
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]
a = Solution()
print(a.evaluateDivision(equations, values, queries))