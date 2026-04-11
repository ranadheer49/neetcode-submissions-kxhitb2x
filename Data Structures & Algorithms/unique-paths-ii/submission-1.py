class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows,cols = len(obstacleGrid), len(obstacleGrid[0])
        table = [[0] * cols for _ in range(rows)]

        if obstacleGrid[0][0] == 1:
            return 0

        for i in range(cols):
            if obstacleGrid[0][i]== 1:
                break
            table[0][i] = 1

        for j in range(rows):
            if obstacleGrid[j][0] == 1:
                break
            table[j][0]= 1


        for row in range(1,rows):
            for col in range(1,cols):
                if obstacleGrid[row][col] != 1:
                    table[row][col] = table[row-1][col]+table[row][col-1]


        return table[rows-1][cols-1]            

        