class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        results = []
        tempTemperature=temperatures
        for i, item in enumerate(temperatures):
            tempData = tempTemperature
            startingIndex = i
            found = False
            breakLoop = False
            while breakLoop == False:
                data = tempData[startingIndex]
                if data>item:
                    results.append(startingIndex-i)
                    found = True
                    breakLoop = True
                startingIndex+=1
                if len(tempTemperature) <= startingIndex:
                    breakLoop=True
            if found == False:
                results.append(0)
        return results

            
        