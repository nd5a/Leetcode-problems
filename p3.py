def maxProduct(nums):
    prod = 0
    for i in nums:
        while i > 0:
            prod *= i % 10
            i //= 10
    return prod        

nums=[2,3,-2,4]
print(maxProduct(nums))