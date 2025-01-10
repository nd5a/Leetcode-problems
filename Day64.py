# Words Subsets

from collections import Counter
class Solution:
    def wordSubsets(self, words1, words2):
        max_count = Counter()
        for word in words2:
            word_count = Counter(word)
            for char, count in word_count.items():
                max_count[char] = max(max_count[char], count)

        result = []
        for word in words1:
            word_count = Counter(word)
            
            if all(word_count[char] >= count for char, count in max_count.items()):
                result.append(word)

        return result
