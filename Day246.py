# Valid Word

class Solution:
    def isValid(self, word):
        vowels = set("aeiouAEIOU")
        consonants = set("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ")
        
        if len(word) < 3:
            return False

        has_vowel = False
        has_consonant = False

        for ch in word:
            if not ch.isalnum():
                return False 
            if ch in vowels:
                has_vowel = True
            elif ch in consonants:
                has_consonant = True

        return has_vowel and has_consonant
