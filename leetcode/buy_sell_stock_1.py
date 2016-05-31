import sys

def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    minPrice = 0
    maxProfit = 0
    if len(prices) > 1:
        for i in range(0, len(prices)):
            minPrice = min(minPrice, prices[i])
            maxProfit = max(maxProfit, prices[i] - minPrice)
        return maxProfit
    else:
        return maxProfit

print(maxProfit([1,2]))
