# Minimum Number of Operations to Move All Balls to Each Box
class Solution:
    def minOperations(self, boxes):
        N = len(boxes)
        ans = [0] * N

        for i in range(N):
            for j in range(N):
                if boxes[j] == "1":
                    ans[i] += abs(j - i)
        return ans