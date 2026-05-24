class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        sum_data = {}
        freq_data = [[] for _ in range(len(nums) + 1)]
        for data in nums:
            sum_data[data] = 1 + sum_data.get(data, 0)

        for key, v in sum_data.items():
            freq_data[v].append(key)
        response_data = []
        for i in range(len(freq_data) - 1, 0, -1):
            for num in freq_data[i]:
                response_data.append(num)
                if len(response_data) == k:
                    return response_data

        

        


        
        