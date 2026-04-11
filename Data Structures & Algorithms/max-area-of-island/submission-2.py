class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        neighbours = [(0,1), (1,0), (0,-1),(-1,0)]
        rows,cols = len(grid),len(grid[0])

        def dfs(r,c):
            if r >= rows or r < 0 or c >= cols or c < 0 or grid[r][c] == 0:
                return 0
            area  = 1
            grid[r][c] = 0
            for nr,nc in neighbours:
                area += dfs(r+nr, c+nc)

            # maxArea = max(maxArea,localArea)
            return area

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    maxArea = max(dfs(i,j),maxArea)

        return maxArea                            

        