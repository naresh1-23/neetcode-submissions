class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        conZero = 0
        for i in nums:
            prod *= i if i != 0 else 1
            conZero +=1 if i ==0 else 0
        result =  [0]* len(nums)
        if conZero>1: return result
        for io, j in enumerate(nums):
            if conZero: result[io] = 0 if j else prod
            else: result[io] = prod // j
        return result
            


        