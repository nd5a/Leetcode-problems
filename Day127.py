# Maximum Candies Allocated to K Children

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k:
            return 0 
        
        left, right = 1, max(candies)
        
        def canAllocate(mid: int) -> bool:
            count = sum(c // mid for c in candies)
            return count >= k
        
        result = 0
        while left <= right:
            mid = (left + right) // 2
            if canAllocate(mid):
                result = mid
                left = mid + 1  
            else:
                right = mid - 1 
        
        return result