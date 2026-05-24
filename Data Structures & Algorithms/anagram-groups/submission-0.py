class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_data = {}
        for data in strs:
            sorted_str = ''.join(sorted(data))
            if sorted_str in sorted_data:
                sorted_data[sorted_str].append(data)
            else:
                sorted_data[sorted_str] = [data]
        result_data = []
        for ley, value in sorted_data.items():
            result_data.append(value)
        return result_data
        