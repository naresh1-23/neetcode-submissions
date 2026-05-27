import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_text = re.sub(r'[^a-zA-Z0-9]', '', s)
        cleaned_text = cleaned_text.lower()
        end = len(cleaned_text) -1 
        start = 0
        while end>=start:
            if cleaned_text[end]!=cleaned_text[start]:
                return False
            end-=1
            start+=1
        return True
        