# Valid Sudoku

class Solution:
    def isValidSudoku(self, board):
        R = len(board)
        C = len(board[0])

        rows = [[False] * 9 for _ in range(R)]
        cols = [[False] * 9 for _ in range(C)]
        cells = [[False] * 9 for _ in range(R * C // 9)]

        for i in range(R):
            for j in range(C):
                if board[i][j] == ".":
                    continue
                
                x = int(board[i][j]) - 1
                if rows[i][x]:
                    return False
                if cols[j][x]:
                    return False
                
                bigi = i // 3
                bigj = j // 3

                if cells[bigi * 3 + bigj][x]:
                    return False
                
                rows[i][x] = cols[j][x] = cells[bigi * 3 + bigj][x] = True
        return True