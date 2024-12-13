nums = [1, 2, 3, 1]
k = 3
def containsNearbyDuplicate(nums, k):
    s = set()
    for i in range(len(nums)):
        if nums[i] in s and i - s[nums[i]] <= k:
            return True
        s[nums[i]] = i
    return False
print(containsNearbyDuplicate(nums, k))
print(containsNearbyDuplicate([1, 2, 3, 1],
3))  # True
