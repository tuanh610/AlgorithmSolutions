class Node:
    def __init__(self, val):
        self.val = val
        self.adjNodes = []
        self.visited = False
        self.parent = None

    def __str__(self):
        return str(self.val)

class Solution:
    def route(self, node1, node2):
        queue = [node1]
        while len(queue) > 0:
            cur = queue.pop(0)
            cur.visited = True
            if cur == node2:
                res = []
                while cur is not None:
                    res.append(cur)
                    cur = cur.parent
                res.reverse()
                return res
            for adj in cur.adjNodes:
                if not adj.visited:
                    if adj.parent is None:
                        adj.parent = cur
                    queue.append(adj)
        return None

#Input
nodes = [Node(i) for i in range(1, 6)]
nodes[0].adjNodes = [nodes[1],nodes[2]]
nodes[1].adjNodes = [nodes[3]]
nodes[2].adjNodes = [nodes[4]]
nodes[3].adjNodes = [nodes[2], nodes[4]]
#Test
a = Solution()
temp = a.route(nodes[0], nodes[4])
if temp is None:
    print("No route")
else:
    for node in temp:
        print(node)