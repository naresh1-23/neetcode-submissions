import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        ans = None
        while l<=r:
            mid = (l+r)//2
            hour = 0
            for i in piles:
                data = math.ceil(i/mid) 
                hour+=data
            if hour <=h:
                ans = mid
                r = mid-1
            else:
                l = mid+1
        return ans