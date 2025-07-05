# Find the K-th Character in String Game II

class Solution:
    def kthCharacter(self, k, operations):
        k -= 1
        current = 0

        for index, op in enumerate(operations):
            if ((1 << index) & k) > 0:
                if op == 1:
                    current = ( current + 1) % 26
        return chr(current + ord('a'))