class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        first_data = {}
        second_data = {}
        for data in range(len(s)):
            first_data[s[data]] = 1+ first_data.get(s[data],0)
            second_data[t[data]] = 1+ second_data.get(t[data],0)
        return first_data == second_data
        

        