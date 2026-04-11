class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0]*n for _ in range(2)]
        rows,cols = m,n
        for c in range(cols):
            grid[0][c] = 1
        # for r in range(rows):
        #     grid[r][0] = 1    
        
        for r in range(1,rows):
            grid[r%2][0]= 1
            for c in range(1,cols):
                grid[r%2][c] = grid[(r-1)%2][c] + grid[r%2][c-1]

        return grid[(m-1)%2][n-1]        
        