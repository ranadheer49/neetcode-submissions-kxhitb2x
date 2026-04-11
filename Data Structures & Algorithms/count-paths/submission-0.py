class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0]*n for _ in range(m)]
        rows,cols = m,n
        for c in range(cols):
            grid[0][c] = 1
        for r in range(rows):
            grid[r][0] = 1    
        
        for r in range(1,rows):
            for c in range(1,cols):
                grid[r][c] = grid[r-1][c] + grid[r][c-1]

        return grid[m-1][n-1]        
        