# Water Bottles II

class Solution(object):
    def maxBottlesDrunk(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        empty = 0
        count = 0

        while numBottles > 0:
            empty += numBottles
            count += numBottles
            numBottles = 0

            if empty >= numExchange:
                numBottles += 1
                empty -= numExchange
                numExchange += 1
        return count