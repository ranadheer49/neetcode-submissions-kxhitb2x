class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        rows, cols = len(grid) , len(grid[0])
        dir = [[-1,0],[1,0],[0,-1],[0,1]]

        def bfs(r,c):
            q = deque()                  # ["0","0","0","0","0"],  count = 1  (2,1),(0,3),(2,0)
            grid[r][c] = '0'            #  ["0","0","0","0","0"],
            q.append((r,c))             #  ["0","0","0","0","0"],
            while q:                    #  ["0","0","0","0","0"]
                r ,c  = q.popleft()
                for i,j in dir:
                    nr = r + i
                    nc = c + j
                    if min(nr,nc) >= 0 and nr < rows and nc < cols and grid[nr][nc] == '1':
                        grid[nr][nc] = '0'
                        q.append((nr,nc))

            return 

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    count += 1
                    bfs(r,c)

        return count                            

        