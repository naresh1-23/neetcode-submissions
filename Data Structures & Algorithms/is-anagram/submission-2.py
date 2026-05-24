class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first_data = {}
        second_data = {}
        for data in s:
            if data in first_data:
                first_data[data] += 1
            else:
                first_data[data] = 1

        for data in t:
            if data in second_data:
                second_data[data] += 1
            else:
                second_data[data] = 1
        return first_data == second_data
        

        