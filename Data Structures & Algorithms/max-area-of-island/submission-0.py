class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0

        def neighbours(r,c):
            n =[]
            if r+1 < len(grid):
                n.append((r+1,c))
            if c+1 < len(grid[0]):
                n.append((r,c+1))
            if r-1 >= 0:
                n.append((r-1,c))
            if c-1 >= 0:
                n.append((r,c-1))
            return n                

        def bfs(r,c):
            q = deque()
            q.append((r,c))
            grid[r][c] = 0
            localArea = 1

            while q:
                cr,cc = q.popleft()

                for nr,nc in neighbours(cr,cc):
                    if grid[nr][nc] == 1:
                        localArea += 1
                        grid[nr][nc] = 0
                        q.append((nr,nc))

            # maxArea = max(maxArea,localArea)
            return localArea

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    maxArea = max(bfs(i,j),maxArea)

        return maxArea                            

        