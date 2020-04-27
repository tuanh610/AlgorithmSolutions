class Solution:
    """
    Only right and down transversal is possible
    """
    def findShortestPath(self, row, col, obstacles):
        obs = set()
        for x,y in obstacles:
            obs.add(x*row+y)
        targetX, targetY = row-1, col-1

        def findPath(curX, curY,):
            #basecase
            if curX == targetX and curY == targetY:
                return [(curX, curY)]

            path = None
            if curY<col-1 and curX*row+curY+1 not in obs:
                path = findPath(curX, curY+1)
            if path is None and curX<row-1 and (curX+1)*row+curY not in obs:
                path = findPath(curX+1, curY)
            if path is not None:
                path.append((curX, curY))
            return path

        path = findPath(0,0)
        path.reverse()
        return path


if __name__ == '__main__':
    A = Solution()
    row = 6
    col = 6
    obs = [(0,4), (1,3), (2,2), (2,4), (4,1), (4,4), (5,2), (3,3)]
    print(A.findShortestPath(row, col, obs))