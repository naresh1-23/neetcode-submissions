class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        data = []
        for n in nums:
            if n in data:
                return True
            data.append(n)
        return False