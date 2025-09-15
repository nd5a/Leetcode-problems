# Maximum Number of Words you can type

class Solution:
    def canBeTypedWords(self, text, brokenLetters):
        broken = set(brokenLetters)
        def can(word):
            for c in word:
                if c in broken:
                    return False
            return True

        count= 0
        for word in text.split(" "):
            if can(word):
                count += 1
        return count