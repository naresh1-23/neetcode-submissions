class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        fleet = []
        cars = list(zip(position, speed))
        cars.sort(reverse=True)
        for i in range(n):
            time = (target-cars[i][0])/cars[i][1]
            if not fleet:
                fleet.append(time)
                continue
            
            popedData = fleet.pop()
            fleet.append(popedData)
            if time>popedData:
                fleet.append(time)
        return len(fleet)
                


        