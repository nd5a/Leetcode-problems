# Sliding Puzzle

from typing import List
import collections

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        R = len(board)
        C = len(board[0])

        def h(b):
            return "".join(str(b[i][j]) for i in range(R) for j in range(C))

        # Preprocess target state
        target = [[1, 2, 3], [4, 5, 0]]
        target_hash = h(target)

        # Possible directions to move the empty space (0)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # Preprocess: Find all possible configurations from the target
        def preprocess():
            dist = {}
            q = collections.deque()
            start_x, start_y = 1, 2  # Position of 0 in the target state
            
            # Initialize queue with target state
            dist[target_hash] = 0
            q.append((0, target, start_x, start_y))

            while q:
                d, b, x, y = q.popleft()

                for dx, dy in directions:
                    nx, ny = x + dx, y + dy

                    # Check bounds
                    if 0 <= nx < R and 0 <= ny < C:
                        # Swap empty space with the new position
                        b[x][y], b[nx][ny] = b[nx][ny], b[x][y]
                        board_hash = h(b)

                        # If new state is not visited, add to the queue
                        if board_hash not in dist:
                            dist[board_hash] = d + 1
                            q.append((d + 1, [row[:] for row in b], nx, ny))

                        # Swap back to restore original state
                        b[x][y], b[nx][ny] = b[nx][ny], b[x][y]
            return dist

        # Preprocess distances from the target state
        dist = preprocess()

        # Get hash of the current board state
        current_hash = h(board)

        # Check if the current board state can reach the target
        return dist.get(current_hash, -1)