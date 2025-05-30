# Find Closest Node to Given Two nodes

class Solution:
    def closestMeetingNode(self, edges, node1, node2):
        N = len(edges)
        INF = 10 ** 20

        def traverse(start):
            distances = [INF] * N
            distances[start] = 0

            count = 0
            current = start
            while current != -1:
                distances[current] = count
                count += 1
                current = edges[current]
                if distances[current] != INF:
                    break
            return distances
        d1 = traverse(node1)
        d2 = traverse(node2)

        best = INF
        best_index = 0
        for index, (a, b) in enumerate(zip(d1, d2)):
            if max(a,b) < best:
                best = max(a,b)
                best_index = index
        if best == INF:
            return -1
        return best_index