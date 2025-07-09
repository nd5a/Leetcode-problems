# Reschedule Meetings for Maximum Free Time I

class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime, endTime):
        INF = 10 ** 20
        events = []

        events.append((-INF, 0))
        for s, e in zip(startTime, endTime):
            events.append((s, e))
        events.append((eventTime, INF))
        N = len(events)

        best = 0
        for i in range(1, N - 1):
            best = max(best, events[i + 1][0] - events[i][1])
        
        prefix = [0]
        for i in range(1, N - 1):
            prefix.append(prefix[-1] + events[i][1] - events[i][0])
        
        for i in range(1, N - 1):
            if not (i + k - 1 < N - 1):
                continue

            previous_end_time = events[i - 1][1]
            next_start_time = events[i + k][0]

            empty = next_start_time - previous_end_time

            sum_of_length = prefix[i + k - 1] - prefix[i - 1]

            best = max(best, empty - sum_of_length)
        return best