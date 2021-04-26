from collections import defaultdict
import math
class UndergroundSystem:
    def __init__(self):
        self.checked = defaultdict(list)
        self.times = defaultdict(list)
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if id not in self.checked:
            self.checked[id].append(stationName)
            self.checked[id].append(t)
        else:
            return 'Invalid ID'
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if id in self.checked:
            self.times[(self.checked[id][0],stationName)].append(t-self.checked[id][1])
            self.checked.pop(id)
        else:
            return 'check in first mate'
        
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        average =  sum(self.times[(startStation,endStation)])/len(self.times[(startStation,endStation)])
        return average
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)