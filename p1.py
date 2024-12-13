# from collections import deque

# def longestSubarray(nums, limit):
#     max_deque, min_deque = deque(), deque()
#     left = 0
#     res = 0

#     for right, num in enumerate(nums):
#         # Update the max and min deques
#         while max_deque and nums[max_deque[-1]] < num:
#             max_deque.pop()
#         max_deque.append(right)

#         while min_deque and nums[min_deque[-1]] > num:
#             min_deque.pop()
#         min_deque.append(right)

#         while nums[max_deque[0]] - nums[min_deque[0]] > limit:
#             left += 1
#             if left > max_deque[0]:
#                 max_deque.popleft()
#             if left > min_deque[0]:
#                 min_deque.popleft()

#         res = max(res, right - left + 1)

#     return res

# print(longestSubarray([8, 2, 4, 7], 4))  
# print(longestSubarray([10, 1, 2, 4, 7, 2], 5))  
# print(longestSubarray([4, 2, 2, 2, 4, 4, 2, 2], 0)) 

# Maximum largest sum of subarray problem

# nums = [1,3,-1,3]
# l=[]
# for i in range(len(nums)):
#     if len(nums) == 1:
#         l.append(nums[i])
#     for j in range(i+1,len(nums)+1):
#         l.append(sum(nums[i:j]))
# print(max(l))

# Contains Duplicate

# nums= [1,1,1,3,3,4,3,2,4,2]

# def containsDuplicate(nums):
#         s=set(nums)
#         if len(nums) != len(s):
#             return True
#         else:
#             return False

