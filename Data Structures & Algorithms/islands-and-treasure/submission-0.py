class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        min_map = {}
        def isValid(r,c):
            return min(r,c) >= 0 and r < rows and c < cols and grid[r][c] != -1

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c,0))

        while q:
            r,c,dist = q.popleft()
            nei = [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]

            for nr,nc in nei:
                if isValid(nr,nc) and grid[nr][nc] == 2147483647:
                    grid[nr][nc] = dist + 1
                    q.append((nr,nc,dist+1))
       


