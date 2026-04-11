class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows,cols = len(matrix) , len(matrix[0])
        dp = [[0]* cols for _ in range(rows)]
        globalMax = [0]
        for c in range(cols):
            if matrix[0][c] == "1":
                dp[0][c] = 1
                globalMax[0] = 1

        for r in range(rows):
            if matrix[r][0] == "1":
                dp[r][0] = 1
                globalMax[0] = 1

        for r in range(1,rows):
            for c in range(1,cols):
                if matrix[r][c] == "1":
                    dp[r][c] = 1 + min(dp[r-1][c], dp[r][c-1], dp[r-1][c-1])

                globalMax[0] = max(globalMax[0], dp[r][c])

        return globalMax[0] * globalMax[0]       