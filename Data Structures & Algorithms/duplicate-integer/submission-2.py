class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_data = list(set(nums))
        return True if len(nums) != len(set_data) else False