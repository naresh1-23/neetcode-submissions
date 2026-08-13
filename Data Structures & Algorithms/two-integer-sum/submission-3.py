class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        data = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in data:
                return [data[diff], i]
            data[num] = i