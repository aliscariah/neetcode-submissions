class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i=0
        k=1
        max_profit=0
        while k<len(prices):
            profit=prices[k]-prices[i]
            if profit<=0:
                i=k
            max_profit=max(max_profit,profit)
            k+=1
        return max_profit