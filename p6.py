# # union and inrtersection of two lists
def union(nums1, nums2):
    m=sorted(nums1 + nums2)
    l3=list(set(m))
    return len(m)-len(l3) 
l=[3,7,1,5,9,15,21]
l2=[9,10,16,5,3,27]
print(union(l,l2))

def union(nums1, nums2):
    m=list(set(nums1) & set(nums2))
    return len(m)    
l=[3,7,1,5,9,15,21]
l2=[9,10,16,5,3,27]
print(union(l,l2))

# Wrong Answer
# 2072 / 2094 testcases passed

# Editorial
# Input
# nums1 =
# [1,1]
# nums2 =
# [1,2]

# Use Testcase
# Output
# 1.50000
# Expected
# 1.00000

# # code
# def findMedianSortedArrays(nums1, nums2):
#     merged = sorted(nums1 + nums2)
#     n = len(merged)
#     if n % 2 == 0:
#         return (merged[n // 2 - 1] + merged[n // 2]) /2.0
#     else:
#         return merged[n // 2]