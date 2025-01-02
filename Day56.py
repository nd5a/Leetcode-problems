# Count Vowel Strings in Ranges

class Solution:
    def vowelStrings(self, words, queries):
        vowel = "aeiou"

        prefix = [0]
        for word in words:
            is_wovel_str = (word[0] in vowel and word[-1] in vowel)

            if is_wovel_str:
                prefix.append(prefix[-1] + 1)
            else:
                prefix.append(prefix[-1] + 0)
        
        ans = []
        for l, r in queries:
            ans.append(prefix[r + 1] - prefix[l])
        return ans