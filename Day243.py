# The Earliest and Latest Rounds Where Players Compete

class Solution:
    def earliestAndLatest(self, n, firstPlayer, secondPlayer):
        from functools import lru_cache

        @lru_cache(None)
        def dfs(players, round_num):
            players = list(players)
            m = len(players)

            for i in range(m // 2):
                a = players[i]
                b = players[m - 1 - i]
                if {a, b} == {firstPlayer - 1, secondPlayer - 1}:
                    return round_num, round_num

            next_states = []

            def generate(i, new_list):
                if i >= m // 2:
                    if m % 2 == 1:
                        new_list.append(players[m // 2])
                    next_states.append(tuple(sorted(new_list)))
                    return

                a = players[i]
                b = players[m - 1 - i]

                if {a, b} & {firstPlayer - 1, secondPlayer - 1}:
                    new_list.append(a if a in {firstPlayer - 1, secondPlayer - 1} else b)
                    generate(i + 1, new_list.copy())
                else:
                    generate(i + 1, new_list + [a])
                    generate(i + 1, new_list + [b])

            generate(0, [])

            min_r = float('inf')
            max_r = float('-inf')

            for state in next_states:
                e, l = dfs(state, round_num + 1)
                min_r = min(min_r, e)
                max_r = max(max_r, l)

            return min_r, max_r

        players = tuple(range(n))
        return list(dfs(players, 1))
