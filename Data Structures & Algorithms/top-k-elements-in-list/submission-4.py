class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        sum_data = {}
        for data in nums:
            sum_data[data] = 1 + sum_data.get(data, 0)

        values_only = [item[0] for item in sorted(sum_data.items(), key=lambda item: item[1], reverse=True)[:k]]
        return values_only
        


        
        