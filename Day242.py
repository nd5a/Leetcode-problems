# Meeting Rooms III

class Solution:
    def mostBooked(self, n, meetings):
        import heapq

        meetings.sort()
        count = [0] * n
        available = list(range(n))
        heapq.heapify(available)
        busy = []

        for start, end in meetings:
            while busy and busy[0][0] <= start:
                _, room = heapq.heappop(busy)
                heapq.heappush(available, room)

            if available:
                room = heapq.heappop(available)
                heapq.heappush(busy, (end, room))
                count[room] += 1
            else:
                end_time, room = heapq.heappop(busy)
                new_end = end_time + (end - start)
                heapq.heappush(busy, (new_end, room))
                count[room] += 1

        return count.index(max(count))
