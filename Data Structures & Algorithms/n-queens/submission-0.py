class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        finalList = []
        cols = set()
        leftDiag = set()
        rightDiag = set()
        def isValidPos(r,c,slate):
            if c in cols or r-c in leftDiag or r+c in rightDiag:
                return False

            return True

        def nqHelper(r,slate):
            if r == n:
                finalList.append(["".join(row) for row in slate])
                return 

            for c in range(n):
                if isValidPos(r,c,slate):
                    slate[r][c] = "Q"
                    cols.add(c)
                    leftDiag.add(r-c)
                    rightDiag.add(r + c)
                    nqHelper(r + 1 , slate)
                    slate[r][c] = "."
                    cols.remove(c)
                    leftDiag.remove(r-c)
                    rightDiag.remove(r + c)

                continue    
        slate = [["."]*n for _ in range(n)]
        nqHelper(0,slate)
        return finalList

