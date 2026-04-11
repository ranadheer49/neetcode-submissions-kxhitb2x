class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        table = [[0] * (i + 1) for i in range(numRows)]

        for j in range(numRows):
            table[j][0] = 1
            table[j][len(table[j])-1] = 1

        for r in range(2,numRows):
            for c in range(1, len(table[r])-1):
                table[r][c] = table[r-1][c] + table[r-1][c-1]

        return table           

        