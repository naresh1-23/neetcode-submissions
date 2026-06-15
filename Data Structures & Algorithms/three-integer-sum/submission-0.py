class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        sorted_data = nums.sort()
        for i in range(len(nums)):
            a= nums[i]
            if a > 0:
                break
            if i > 0 and a == nums[i - 1]:
                continue
            l = i+1
            r = len(nums) -1 
            while l < r:
                sumData = a+ nums[l] + nums[r]
                if sumData >0:
                    r-=1
                elif sumData <0 :
                    l+=1
                else:
                    result.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return result
        
        