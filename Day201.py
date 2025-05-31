# Snakes and Ladders

from collections import deque

class Solution:
    def snakesAndLadders(self, board):
        n = len(board)

        def get_board_index(pos: int):

            r = (pos - 1) // n
            c = (pos - 1) % n
            row = n - 1 - r
            col = c if r % 2 == 0 else n - 1 - c
            return row, col

        visited = [False] * (n * n + 1)
        queue = deque([(1, 0)])

        while queue:
            pos, moves = queue.popleft()
            for i in range(1, 7):  
                next_pos = pos + i
                if next_pos > n * n:
                    continue
                row, col = get_board_index(next_pos)
                if board[row][col] != -1:
                    next_pos = board[row][col]

                if next_pos == n * n:
                    return moves + 1

                if not visited[next_pos]:
                    visited[next_pos] = True
                    queue.append((next_pos, moves + 1))

        return -1
