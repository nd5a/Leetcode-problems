# Find Unique Binary String

class Solution:
    def findDifferentBinaryString(self, nums):
        N = len(nums)
        forbidden = set()
        
        for s in nums:
            forbidden.add(int(s, 2))
        for i in range(pow(2, N)):
            if i not in forbidden:
                r = bin(i)[2:]
                while len(r) < N:
                    r = "0" + r
                return r