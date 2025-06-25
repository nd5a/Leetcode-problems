# Kth Smallest Product of Two Sorted Arrays

import bisect
from math import ceil
class Solution:
    def kthSmallestProduct(self, nums1, nums2, k):
        # l1 = len(nums1)
        # l2 = len(nums2)

        # pl = []
        # for i in range(l1):
        #     for j in range(l2):
        #         pl.append(nums1[i] * nums2[j])
        # sort_pl = sorted(pl)
        # return sort_pl[k-1]
        N2 = len(nums2)

        def get_smaller_product(target):
            smaller = 0

            for x in nums1:
                if x < 0:
                    smaller += N2 - bisect.bisect_left(nums2, ceil(target / x))
                elif x == 0:
                    if target >= 0:
                        smaller += N2
                else:
                    smaller += bisect.bisect_right(nums2, target // x)
            return smaller
        
        def good(target):
            return get_smaller_product(target) >= k
        
        left = -10 ** 10
        right = 10 ** 10

        while left < right:
            mid = (left + right) // 2

            if good(mid):
                right = mid
            else:
                left = mid + 1
        
        return left