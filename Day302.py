# Sort Vowels in a string

class Solution:
    def sortVowels(self, s: str) -> str:
        N = len(s)
        vowels = []

        ans = list(s)

        for i in range(N):
            if s[i].lower() in "aeiou":
                vowels.append(i)
        vowels.sort(key = lambda i : s[i])
        count = 0
        for i in range(N):
            if s[i].lower() in "aeiou":
                ans[i] = s[vowels[count]]
                count += 1
        return "".join(ans)