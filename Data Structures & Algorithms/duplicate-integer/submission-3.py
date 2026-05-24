class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        test = {}
        for x in nums:
            if x in test:
                return True
            test[x] = 1
        return False