class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        data = set()
        for d in nums:
            if d in data:
                return True
            data.add(d)
        return False