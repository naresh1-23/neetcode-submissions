class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = []        
        for i, n in enumerate(nums, 0):
            result = 1
            for j, m in enumerate(nums, 0):
                if i == j:
                    continue
                else:
                    result*=m
            prod.append(result)
        return prod