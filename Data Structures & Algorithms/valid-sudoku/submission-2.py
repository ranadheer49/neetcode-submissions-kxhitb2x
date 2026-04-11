class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
     
    #  board =
 #[["1","2",".",".","3",".",".",".","."],
 # ["4",".",".","5",".",".",".",".","."],
  #[".","9","8",".",".",".",".",".","3"],
 # ["5",".",".",".","6",".",".",".","4"],
  #[".",".",".","8",".","3",".",".","5"],
  #["7",".",".",".","2",".",".",".","6"],
  #[".",".",".",".",".",".","2",".","."],
  #[".",".",".","4","1","9",".",".","8"],
  #[".",".",".",".","8",".",".","7","9"]]

#    have a set for each row, each colum and each grid.
#  start traversing board, for each index, check if exists in any of sets or else add it.
#  if exists satisfies then break and return false. else end of traversal return true.
        rows , cols = len(board), len(board[0])
        rowsSet = [set() for _ in range(rows)]
        colSet = [set() for _ in range(cols)]
        gridSet = [set() for _ in range(rows)]

        for r in range(rows):
            for c in range(cols):
                cur = board[r][c]
                if cur == '.':
                    continue
                if cur in rowsSet[r] or cur in colSet[c] or cur in gridSet[(r//3)*3 + c//3]:
                    return False
                else:
                      rowsSet[r].add(cur)
                      colSet[c].add(cur)
                      gridSet[(r//3)*3 + c//3].add(cur)
        return True              
