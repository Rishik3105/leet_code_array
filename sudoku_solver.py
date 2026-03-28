class Solution:
    def solveSudoku(self, board):
        def is_valid(r, c, val):
            for i in range(9):
                if board[r][i] == val:
                    return False
                if board[i][c] == val:
                    return False
                if board[3 * (r // 3) + i // 3][3 * (c // 3) + i % 3] == val:
                    return False
            return True

        def solve():
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        for ch in '123456789':
                            if is_valid(i, j, ch):
                                board[i][j] = ch
                                if solve():
                                    return True
                                board[i][j] = '.'
                        return False
            return True

        solve()
board = [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]

s = Solution()
s.solveSudoku(board)

for row in board:
    print(row)
