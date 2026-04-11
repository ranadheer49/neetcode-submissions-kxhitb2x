class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def nebof(i,j):
            n = []
            if j+1 < len(grid[0]):
                n.append((i,j+1))
            if j-1 >= 0:
                n.append((i,j-1))
            if i+1 < len(grid):
                n.append((i+1,j))
            if i-1 >= 0:
                n.append((i-1,j))
            return n                

        def bfs(x,y):
            q = deque()
            q.append((x,y))
            while q:
                i,j = q.popleft()
                grid[i][j] = 0

                for neighbour in nebof(i,j):
                    x,y = neighbour
                    if grid[x][y] == "1":
                        q.append((x,y))

            return
        island = 0    
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    island += 1
                    bfs(i,j) 
                    

        return island                          


        