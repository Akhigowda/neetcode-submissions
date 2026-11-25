class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        output = 0
        for i in range(len(prices)):
            for j in range(i,len(prices)):
                profit = prices[j] - prices[i]

                output = max(output,profit)
        

        return output