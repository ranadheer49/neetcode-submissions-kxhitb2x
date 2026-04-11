class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # board = [
#   ["A","B","C","D"],
#   ["S","A","A","T"],
#   ["A","C","A","E"]
# ], word = "CAT"   Output: true
        rows , cols = len(board), len(board[0])
        visited = [[0] * cols for _ in range(rows)]
        def helper(wi,r,c):
            if wi == len(word):
                return True

            if min(r,c) < 0 or r >= rows or c >= cols or word[wi] != board[r][c] or visited[r][c] == 1:
                return False
            visited[r][c] = 1    
            res = helper(wi + 1, r +1,c) or helper(wi + 1, r -1,c) or helper(wi + 1, r,c +1) or helper(wi + 1, r,c -1 ) 
            visited[r][c] = 0
            return res

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if helper(0,r,c):
                        return True
        return False    














        