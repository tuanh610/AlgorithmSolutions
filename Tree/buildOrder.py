class Node:
    def __init__(self, val):
        self.val = val
        self.children = []
        self.parent = set()
        self.visited = False

    def __str__(self):
        return str(self.val)

class Solution:
    def buildOrder(self, projects, dependencies):
        data = {}
        for prj in projects:
            data[prj] = Node(prj)
        for parent, child in dependencies:
            data[parent].children.append(data[child])
            data[child].parent.add(parent)
        res = []
        for prj, node in data.items():
            if not node.visited:
                queue = [(node, None)]
                while len(queue) > 0:
                    cur, parentVal = queue.pop(0)
                    if parentVal is not None:
                        cur.parent.remove(parentVal)
                    if len(cur.parent) == 0:
                        res.append(cur.val)
                        cur.visited = True
                        for child in cur.children:
                            if not child.visited:
                                queue.append((child,cur.val))
        for prj in data:
            if data[prj].visited == False:
                return None
        return res

if __name__ == '__main__':
    projects = ["a", "b", "c", "d", "e", "f", "g"]
    dependencies = [["a", "d"], ["f", "b"], ["b", "d"], ["f", "a"], ["d", "c"], ["g", "d"]]
    A = Solution()
    print(A.buildOrder(projects, dependencies))

