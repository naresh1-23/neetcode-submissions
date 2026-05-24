class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        data = {}
        for i in range(0, len(nums)):
            data[nums[i]] = i
        for j in range(0, len(nums)):
            diff = target - nums[j]
            if diff in data and data[diff] != j:
                return [j, data[diff]]