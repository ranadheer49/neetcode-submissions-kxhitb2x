class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        minutes = 0
        q = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
        nei = [[1,0],[-1,0],[0,1],[0,-1]]
        while q:
            count = len(q)
            hasfreshFruit = False
            while count:                
                r,c = q.popleft()
                for nr,nc in nei:
                    cr = r+nr 
                    cc = c +nc
                    if min(cr,cc) >=0  and cr < rows and cc < cols:
                        if grid[cr][cc] == 1:
                            hasfreshFruit = True
                            grid[cr][cc] = 2
                            q.append((cr,cc))
                count -= 1            
            if hasfreshFruit:
                minutes += 1

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1
        return minutes            


        