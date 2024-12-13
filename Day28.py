class Solution(object):
    def addSpaces(self, s, spaces):
        """
        :type s: str
        :type spaces: List[int]
        :rtype: str
        """
        N = len(s)
        space_index = 0
        ans = []
        
        for i in range(N):
            if space_index < len(spaces) and spaces[space_index] == i:
                ans.append(" ")
                space_index += 1

            ans.append(s[i])
        return "".join(ans)