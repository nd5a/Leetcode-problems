class Solution:
    def countUnguarded(self, R: int, C: int, guards, walls) -> int:

        FREE, GUARD, WALL, GUARDED = 0, 1, 2, 3
        board = [[FREE]* C for _ in range(R)]
        for x, y in guards:
            board[x][y] = GUARD
        for x, y in walls:
            board[x][y] = WALL
        
        # Do the Up Direction
        for y in range(C):
            last = FREE
            for x in range(R - 1, -1, -1):
                if board[x][y] == GUARD:
                    last = GUARD
                elif board[x][y] == WALL:
                    last = WALL
                elif board[x][y] == FREE:
                    if last == GUARD:
                        board[x][y] = GUARDED

        # Do the Down Direction
        for y in range(C):
            last = FREE
            for x in range(R):
                if board[x][y] == GUARD:
                    last = GUARD
                elif board[x][y] == WALL:
                    last = WALL
                elif board[x][y] == FREE:
                    if last == GUARD:
                        board[x][y] = GUARDED
        
        # Do the left Direction
        for x in range(R):
            last = FREE
            for y in range(C):
                if board[x][y] == GUARD:
                    last = GUARD
                elif board[x][y] == WALL:
                    last = WALL
                elif board[x][y] == FREE:
                    if last == GUARD:
                        board[x][y] = GUARDED
        # Do the right Direction
        for x in range(R):
            last = FREE
            for y in range(C - 1, -1, -1):
                if board[x][y] == GUARD:
                    last = GUARD
                elif board[x][y] == WALL:
                    last = WALL
                elif board[x][y] == FREE:
                    if last == GUARD:
                        board[x][y] = GUARDED

        free = 0
        for x in range(R):
            for y in range(C):
                if board[x][y] == FREE:
                    free+=1
        return free