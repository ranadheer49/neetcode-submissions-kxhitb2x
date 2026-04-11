class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
#    Input: matrix = 
 #  [["1","0","1","0","0"],
 #   ["1","0","1","1","1"],
 #   ["1","1","1","1","1"],
 #   ["1","0","0","1","0"] ]
#   f((r,c)) = 1 + min(f(r-1,c), f(r,c-1), f(r-1,c-1))
        rows, cols = len(matrix) , len(matrix[0])
        dp = [[0] * cols for _ in range(rows)]
        if not matrix:
            return 0
            
        maxSquare = 0
        for r in range(rows):
            if matrix[r][0] == "1": 
                dp[r][0] = 1
                maxSquare = 1
        for c in range(cols):
            if matrix[0][c] == "1":
                dp[0][c] = 1
                maxSquare = 1

        for r in range(1,rows):
            for c in range(1,cols):
                if matrix[r][c] == "1":
                    dp[r][c] = 1 + min(dp[r-1][c], dp[r][c-1], dp[r-1][c-1]) 
                    maxSquare = max(maxSquare, dp[r][c])

        return maxSquare * maxSquare