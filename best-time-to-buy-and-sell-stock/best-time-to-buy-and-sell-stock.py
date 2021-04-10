class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        minprice = 1e5
        
        for i,val in enumerate(prices):
            minprice = min(val,minprice)
            profit = val - minprice
            maxprofit = max(profit,maxprofit)
            
        return maxprofit
        