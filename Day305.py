# Vowels Spellchecker

class Solution:
    def spellchecker(self, wordlist, queries):
        seen = set(wordlist)
        caps = {}
        vows = {}

        def norm(w):
            ans = []
            for c in w.lower():
                if c in "aeiou":
                    ans.append("*")
                else:
                    ans.append(c)
            return "".join(ans)

        for word in reversed(wordlist):
            caps[word.lower()] = word
            vows[norm(word)] = word
        
        ans = []
        for q in queries:
            if q in seen:
                ans.append(q)
                continue
            
            if q.lower() in caps:
                ans.append(caps[q.lower()])
                continue
            
            vnorm = norm(q)
            if vnorm in vows:
                ans.append(vows[vnorm])
                continue
            
            ans.append("")
        return ans
        