class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        r = len(s1) - 1
        if len(s1) > len(s2):
            return False
        s1Dict = {char: s1.count(char) for char in set(s1)}
        while r!= len(s2):
            subStr = s2[l:r+1]
            subStrDict =  {char: subStr.count(char) for char in set(subStr)}
            if subStrDict == s1Dict:
                return True
            l+=1
            r+=1
        return False
        