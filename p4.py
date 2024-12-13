# Sum of two Elements in list

# code
# Give all the posible combination of sum that equal target
def two_sum(nums, target):
    nums.sort()
    left = 0
    right = len(nums) - 1
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return [nums[left], nums[right]]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return []

# def sum_of_elements(l,t):
#     for i in range(len(l)):
#         for j in range(i+1,len(l)):
#             if l[i]+l[j]==t:
#                 return [i,j]
#     return None
