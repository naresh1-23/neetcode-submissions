class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        l =0 
        r = 1
        if len(nums) == 1:
            return nums[0]
        while r<len(nums):
            if nums[r] in nums[l:r]:
                return nums[r]
            r+=1
        

        # Floyds algorithm
        # slow = nums[0]
        # fast = nums[0]
        # while True:
        #     slow = nums[slow]
        #     fast = nums[nums[fast]]
        #     if slow == fast:
        #         break
        # slow = nums[0]
        # while slow!=fast:
        #     slow = nums[slow]
        #     fast = nums[fast]

        # return slow