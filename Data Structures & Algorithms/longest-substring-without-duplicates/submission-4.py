class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longestLength = 0
        n = len(s)
        print(n)
        if n==0:
            return 0
        if n == 1:
            return 1
        l = 0
        r=1
        subStr = s[0]
        while r!=n:
            if s[r] in subStr:
                lenStr = len(subStr)
                if longestLength < lenStr:
                    longestLength = lenStr 
                l+=1
                r=l+1
                subStr = s[l]
            else:
                subStr += s[r]
                lenStr = len(subStr)
                if longestLength < lenStr:
                    longestLength = lenStr 
                r+=1
        return longestLength

                

        