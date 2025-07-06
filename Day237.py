# Finding pairs with a Certain Sum

import collections
class FindSumPairs:

    def __init__(self, nums1, nums2):
        self.nums1 = nums1
        self.nums2 = nums2
        self.f2 = collections.Counter(nums2)

    def add(self, index: int, val: int) -> None:
        prev = self.nums2[index]
        self.nums2[index] += val
        after = self.nums2[index]

        self.f2[prev] -= 1
        self.f2[after] += 1

    def count(self, tot: int) -> int:
        c = 0
        for x in self.nums1:
            c += self.f2[tot - x]
        return c


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)