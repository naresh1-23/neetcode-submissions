class Solution:
    def isValid(self, s: str) -> bool:
        array_data = []
        mapped_data = {
            "}" : "{",
            "]" : "[",
            ")" : "("
        }
        for data in s:
            if data in ['(', '[', '{']:
                array_data.append(data)
            elif data in [")", "]", "}"]:
                if not array_data:
                    return False
                last_data = array_data.pop()
                if mapped_data.get(data) != last_data:
                    return False
        return False if array_data else True

                    
        