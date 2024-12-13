class Solution(object):
    def takeCharacters(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if k == 0:
            return 0

        n = len(s)

        # Count occurrences of 'a', 'b', 'c' in the string
        ac = s.count("a")
        bc = s.count("b")
        cc = s.count("c")

        # If there aren't enough of any character, return -1
        if ac < k or bc < k or cc < k:
            return -1

        # Sliding window
        best = n
        left = 0
        lefta = leftb = leftc = 0
        righta, rightb, rightc = ac, bc, cc

        for right in range(n):
            # Decrease the count of the current character from the right segment
            if s[right] == "a":
                righta -= 1
            elif s[right] == "b":
                rightb -= 1
            elif s[right] == "c":
                rightc -= 1

            # Move left pointer to satisfy the condition
            while left <= right and not (lefta + righta >= k and leftb + rightb >= k and leftc + rightc >= k):
                if s[left] == "a":
                    lefta += 1
                elif s[left] == "b":
                    leftb += 1
                elif s[left] == "c":
                    leftc += 1
                left += 1

            # Update the minimum segment length
            if lefta + righta >= k and leftb + rightb >= k and leftc + rightc >= k:
                best = min(best, left + (n - right - 1))

        return best
