class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_data = list(set(nums))
        nums.sort()
        set_data.sort()
        return True if nums != set_data else False
        