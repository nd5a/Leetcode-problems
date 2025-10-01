# Water Bottles

class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        count = 0
        emptyBottles = 0

        while True:
            emptyBottles += numBottles
            count += numBottles

            newExchanged, leftovers = divmod(emptyBottles, numExchange)
            if newExchanged == 0:
                break
            
            emptyBottles = leftovers
            numBottles = newExchanged
        return count