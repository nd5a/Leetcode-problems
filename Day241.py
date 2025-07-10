# Reschedule Meetings for Maximum Free Time II

from sortedcontainers import SortedList
class Solution:
    def maxFreeTime(self, eventTime: int, startTime, endTime):
        INF = 10 ** 20
        events = []

        events.append((-INF, 0))
        for s, e in zip(startTime, endTime):
            events.append((s, e))
        events.append((eventTime, INF))
        N = len(events)

        spaces = SortedList()
        for i in range(N - 1):
            spaces.add(events[i + 1][0] - events[i][1])
        
        best = spaces[-1]
        for i in range(1, N - 1):
            total_space = events[i + 1][0] - events[i-1][1]
            current_space = events[i][1] - events[i][0]

            best = max(best, total_space - current_space)

            spaces.remove(events[i + 1][0] - events[i][1])
            spaces.remove(events[i][0] - events[i -1][1])

            if spaces.bisect_left(current_space) < len(spaces):
                best = max(best, total_space)
            
            spaces.add(events[i + 1][0] - events[i][1])
            spaces.add(events[i][0] - events[i -1][1])

        return best