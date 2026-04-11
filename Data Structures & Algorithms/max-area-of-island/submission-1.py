class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        neighbours = [(0,1), (1,0), (0,-1),(-1,0)]
        rows,cols = len(grid),len(grid[0])

        def bfs(r,c):
            q = deque()
            q.append((r,c))
            grid[r][c] = 0
            localArea = 1

            while q:
                cr,cc = q.popleft()

                for nr,nc in neighbours:
                    nr = nr + cr
                    nc = nc+ cc
                    if 0<= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        localArea += 1
                        grid[nr][nc] = 0
                        q.append((nr,nc))

            # maxArea = max(maxArea,localArea)
            return localArea

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    maxArea = max(bfs(i,j),maxArea)

        return maxArea                            

        