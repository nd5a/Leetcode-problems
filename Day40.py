# Construct String With Repeat Limit

import heapq

class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1

        # Create a max heap
        max_heap = [(-ord(char), count) for char, count in freq.items()]
        heapq.heapify(max_heap)

        result = []

        while max_heap:
            # Get the character with the highest lexicographical order
            char1_freq, count1 = heapq.heappop(max_heap)
            char1 = chr(-char1_freq)

            if len(result) >= repeatLimit and result[-repeatLimit:].count(char1) == repeatLimit:
                if not max_heap:
                    break
                # Use the next lexicographically smaller character
                char2_freq, count2 = heapq.heappop(max_heap)
                char2 = chr(-char2_freq)

                result.append(char2)
                count2 -= 1

                if count2 > 0:
                    heapq.heappush(max_heap, (-ord(char2), count2))

                heapq.heappush(max_heap, (-ord(char1), count1))
            else:
                use_count = min(count1, repeatLimit)
                result.extend([char1] * use_count)
                count1 -= use_count

                if count1 > 0:
                    heapq.heappush(max_heap, (-ord(char1), count1))

        return ''.join(result)
