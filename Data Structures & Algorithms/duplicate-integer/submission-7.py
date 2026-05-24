class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        data = {}
        for d in nums:
            if d in data:
                return True
            data[d] = 1
        return False