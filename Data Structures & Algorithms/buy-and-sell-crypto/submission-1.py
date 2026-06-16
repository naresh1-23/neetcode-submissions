class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n <=1:
            return 0
        result = 0
        l = 0
        r = 1
        while r != n:
            if prices[l]>prices[r]:
                l +=1
                r=l+1
                continue
            temp = prices[r] - prices[l]
            if result <temp:
                result = temp
            r+=1
        return result

        