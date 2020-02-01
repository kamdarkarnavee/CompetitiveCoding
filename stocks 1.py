class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_ = 0
        max_ = 0
        diff = 0
        for i in range(len(prices)):
            if i == 0:
                min_ = prices[i]
                max_ = -1
            else:
                if prices[i] < min_:
                    min_ = prices[i]
                    max_ = prices[i]

                if prices[i] > max_ and diff < prices[i] - min_:
                    max_ = prices[i]
                    diff = max_ - min_
        return diff
