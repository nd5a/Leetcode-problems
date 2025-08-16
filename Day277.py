# Maximum 69 Number

class Solution:
    def maximum69Number (self, num):
        s = str(num)
        if "6" not in s:
            return num
        
        index = s.index("6")
        return int(s[:index] + "9" + s[index + 1:])