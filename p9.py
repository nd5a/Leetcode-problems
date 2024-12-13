# Find the Power of K-Size Subarrays I

class Solution(object):
    def resultsArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        l = []
        for i in range(len(nums) - k + 1):  
            subarray = nums[i:i + k]  
            reversed_subarray = subarray[::-1] 

            if subarray == reversed_subarray:  
                l.append(max(subarray) if len(subarray) == 1 else -1)
            elif subarray == sorted(subarray):  
                if all(subarray[j] + 1 == subarray[j + 1] for j in range(len(subarray) - 1)):
                    l.append(max(subarray))
                else:
                    l.append(-1)
            else:
                l.append(-1)

        return l