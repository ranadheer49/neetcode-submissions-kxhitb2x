class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        l = len(triangle)

        if len(triangle) == 1:
            return triangle[0][0]


        # for r in range(1,len(triangle)):
        #     triangle[r][0] = triangle[r][0] + triangle[r-1][0]
        #     triangle[r][r] = triangle[r][r] + triangle[r-1][r-1]

        
        for r in range(1,len(triangle)):
            for c in range(len(triangle[r])):
                if c == 0:
                    triangle[r][c] = triangle[r][c] + triangle[r -1][c]
                elif c == r:
                    triangle[r][c] = triangle[r][c] + triangle[r -1][c - 1]
                else:     
                    triangle[r][c] = triangle[r][c] + min(triangle[r-1][c-1], triangle[r-1][c])
        # minSum = math.inf

        # for i in range(l):
        #     minSum = min(minSum, triangle[l-1][i])

        return  min(triangle[-1])           
        