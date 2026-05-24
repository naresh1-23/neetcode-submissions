class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_data = set(nums)
        return len(set_data) != len(nums)