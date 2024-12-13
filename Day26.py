class Solution:
    def checkIfExist(self, arr):
        seen = set()

        for num in arr:
            # Check if double or half exists in the set
            if num * 2 in seen or (num % 2 == 0 and num // 2 in seen):
                return True
            seen.add(num)

        return False

