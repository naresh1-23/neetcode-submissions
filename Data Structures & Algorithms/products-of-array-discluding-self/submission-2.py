class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_prod = []
        suffix_prod = []

        for i in range(len(nums)):
            prod = 1
            iteration = 0
            while iteration!=i:
                prod*=nums[iteration]
                iteration+=1
            prefix_prod.append(prod)

            prod = 1
            iteration = len(nums)-1
            while iteration!=i:
                prod*=nums[iteration]
                iteration-=1
            suffix_prod.append(prod)

        res = []
        for i in range(len(nums)):
            res.append(prefix_prod[i]*suffix_prod[i])
        return res
