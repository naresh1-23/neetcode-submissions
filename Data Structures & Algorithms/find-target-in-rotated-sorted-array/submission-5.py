class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        n = len(nums)
        r = n-1
        if n == 0:
            return -1
        if n == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        while l<=r:
            m = (l+r)//2
            if nums[m] == target:
                return m

            if nums[l] <=nums[m]:
                if nums[l] <= target <= nums[m]:
                    r = m-1
                else:
                    l= m+1
            else:
                if nums[m] <= target <= nums[r]:
                    l=m+1
                else:
                    r = m-1

                
        return -1
        