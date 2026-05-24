class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first_set = {}
        for x in s:
            if x in first_set:
                first_set[x]  = first_set[x] + 1
            else:
                first_set[x] = 1
        second_set = {}
        for y in t:
            if y in second_set:
                second_set[y] = second_set[y] +1
            else:
                second_set[y] = 1
        return True if first_set == second_set else False
        