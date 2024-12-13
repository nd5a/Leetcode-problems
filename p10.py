from collections import deque
def shortestSubarray(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dq = deque()
        n = len(nums)
        prefix_sums = [0]
        result = float('inf') 
        
        for num in nums: 
            prefix_sums.append(prefix_sums[-1] + num) 
        
        for i in range(n + 1):
            while dq and prefix_sums[i] - prefix_sums[dq[0]] >= k:
                result = min(result, i - dq.popleft())
        
            while dq and prefix_sums[i] <= prefix_sums[dq[-1]]:
                dq.pop()
                
            dq.append(i)
        
        return result if result != float('inf') else -1
print(shortestSubarray([2,4,20,45,19],19))