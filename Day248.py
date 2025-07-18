# # Find the Maximum Length of valid Subsequence II

# class Solution:
#     def maximumLength(self, nums, k):
#         N = len(nums)
#         for i in range(N):
#             nums[i] %= k
        
#         best = 0
#         # solve every "value" from 0 to k - 1 inclusive
#         for v in range(k):
#             # longest[i] subsequence where the last element is i.
#             longest = [0] * k

#             # value has to be v
#             for x in nums:
#                 prev = (v - x) % k
#                 longest[x] = max(longest[x], longest[prev] + 1)
            
#             best = max(best, max(longest))
#         return best


arr = [5,4,-1,7,8]
# n = len(arr)

# res = [1] * n
# # left = 1
# # for i in range(n):
# #     res[i] = left
# #     left *= arr[i]
# print(str(arr))
# right = 1
# for i in range(n-1, -1, -1):
#     res[i] += right
#     right += arr[i]
# print(res)

# Subarray Sum

currSum = 0
maxSum = float('-inf')
for i in range(len(arr)):
    currSum += arr[i]
    maxSum = max(currSum, maxSum)
    if currSum < 0:
        currSum = 0
print(maxSum)