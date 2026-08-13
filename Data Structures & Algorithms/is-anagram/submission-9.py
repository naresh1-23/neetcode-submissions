class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        firstStringCount = {}
        secondStringCount = {}
        for i in s:
            firstStringCount[i] = firstStringCount.get(i, 0) +1
        for j in t:
            secondStringCount[j] = secondStringCount.get(j, 0) +1
        return firstStringCount == secondStringCount

        