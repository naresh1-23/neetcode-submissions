class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {
            "}" : "{",
            "]" : "[",
            ")" : "("
        }
        for data in s:
            if data in closeToOpen:
                if stack and stack[-1] == closeToOpen[data]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(data)
        return False if stack else True

                    
        