# Push Dominoes

from collections import deque

class Solution:
    def pushDominoes(self, dominoes):
        n = len(dominoes)
        domi = list(dominoes)
        time = [None] * n
        force = [None] * n
        q = deque()

        for i, d in enumerate(domi):
            if d != '.':
                q.append((i, d, 0))
                time[i] = 0
                force[i] = d

        while q:
            i, f, t = q.popleft()
            if f == 'L':
                ni = i - 1
                if ni >= 0:
                    if time[ni] is None:
                        q.append((ni, 'L', t + 1))
                        domi[ni] = 'L'
                        time[ni] = t + 1
                        force[ni] = 'L'
                    elif time[ni] == t + 1 and force[ni] == 'R':
                        domi[ni] = '.'
            elif f == 'R':
                ni = i + 1
                if ni < n:
                    if time[ni] is None:
                        q.append((ni, 'R', t + 1))
                        domi[ni] = 'R'
                        time[ni] = t + 1
                        force[ni] = 'R'
                    elif time[ni] == t + 1 and force[ni] == 'L':
                        domi[ni] = '.'

        return ''.join(domi)