class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        buy = [prices[0]]
        calculate = [0]

        for i in prices[1::]: 

            profitcount = []
            sell = i
            profit = sell - min(buy)
            profitcount.append(profit)
            big = max(profitcount)
            calculate.append(big)
            buy.append(i)

        if max(calculate) >= 0:
            return max(calculate)
        else:
            return 0
