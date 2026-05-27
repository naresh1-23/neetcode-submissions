class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start, end=0,1
        while start<end:
            if len(numbers) == end or numbers[start] + numbers[end] > target:
                start+=1
                end=start+1
            if numbers[start] + numbers[end] == target:
                return [start+1, end+1]

            
            if numbers[start] + numbers[end] < target:
                end+=1