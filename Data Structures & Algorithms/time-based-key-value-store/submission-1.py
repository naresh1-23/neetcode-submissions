class TimeMap:

    def __init__(self):
        self.data = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        arrayData = self.data.get(key, [])
        arrayData.append([timestamp, value])
        self.data[key] = arrayData

    def get(self, key: str, timestamp: int) -> str:
        values = self.data.get(key) or []
        if not values:
            return ""
        l = 0
        r = len(values)-1
        answer = ""
        while l<=r:
            m = (l+r)//2
            if values[m][0] <= timestamp:
                answer = values[m][1]
                l = m + 1
            else:
                r = m - 1

        return answer
        
        
