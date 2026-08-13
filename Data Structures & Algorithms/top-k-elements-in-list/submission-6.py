class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        sumData = {}
        freq = [[] for _ in range(len(nums)+1)]
        for i in nums:
            sumData[i] = sumData.get(i, 0) +1
        
        for key, value in sumData.items():
            freq[value].append(key)
        
        result = []

        for j in range(len(freq)-1, 0, -1):
            for num in freq[j]:
                result.append(num)
                if len(result) == k:
                    return result


        


        
        