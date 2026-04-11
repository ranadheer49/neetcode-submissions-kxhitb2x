class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #  using bit wise operations to find if valid sudoku
        #  will maintain a bit wise integer for row, col and 3 x 3 group.
        # go through each cell check all conditions

        row = [0] * 9
        col = [0] * 9
        squares = [0] * 9

        
        for i in range(9):
            for j in range(9):
                
                if board[i][j] == ".":
                    continue
                val = int(board[i][j]) - 1

                if 1 << val & row[i]:
                    return False

                if 1 << val & col[j]:
                    return False
                if (1 << val) & squares[(i // 3 ) * 3 + (j // 3)]:
                    return False

                row[i] |= (1 << val)
                col[j] |= (1 << val)
                squares[(i // 3)*3 + (j // 3)] |= (1 << val)  

        return True        


        