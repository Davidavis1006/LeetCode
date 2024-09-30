class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # variation of Kadane's Algorithm
        buy=prices[0]
        profit=0

        for i in range(1, len(prices)):
            if prices[i]<buy:
                buy=prices[i]
            elif prices[i]-buy>profit: # if prices[i]>=buy, check the difference and update profit
                profit=prices[i]-buy
        
        return profit