class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1: return intervals
        si = sorted(intervals, key = lambda x: x[0])
        merged = []
        temp = si[0]
        count = 1
        while True:
            if temp[-1]>=si[count][0]:
                temp = [temp[0],max(si[count][-1],temp[-1])]
                count += 1
                if count>=len(si):
                    merged.append(temp)
                    return merged
                
            else:
                merged.append(temp)
                temp = si[count]
                count += 1
                if count>=len(si):
                    merged.append(temp)
                    return merged
                
        
        
                
            
        
        
            
        
        