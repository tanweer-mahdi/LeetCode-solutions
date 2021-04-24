class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # I will overwrite grid
        visit = collections.deque()
        visit.append((0,0)) # starting node
        if len(grid) == 1:
            return 1 if grid[0][0] == 0 else -1
        
        if grid[0][0] != 0 or grid[-1][-1] != 0: return -1
        grid[0][0] = 1
        
        while visit:
            a,b = visit.popleft()
            distance = grid[a][b]
            directions = [[a+1,b+1],[a-1,b-1],[a-1,b+1],[a+1,b-1],[a,b+1],[a+1,b],[a,b-1],[a-1,b]]
            
            for dirr in directions:
                c,d = dirr
                if c>= 0 and c<len(grid) and d>=0 and d<len(grid[0]):
                    if grid[c][d] == 0:
                        if c == len(grid)-1 and d == len(grid[0])-1: 
                            return distance + 1
                        grid[c][d] = distance + 1
                        visit.append((c,d))
                        
        return -1
                    
                    
        