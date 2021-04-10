class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island = 0
        row = len(grid)
        col = len(grid[0])
        visited = set()
        
        ## breadth first search method
        
        def bfs(i,j):
            visit = collections.deque()
            visit.append((i,j))
            
            while visit:
                v = visit.popleft()
                if v not in visited:
                    visited.add(v)
                    a,b = v
                    directions = [[a+1,b],[a-1,b],[a,b+1],[a,b-1]]
                    
                    for dirr in directions:
                        x,y = dirr
                        if x >= 0 and y >=0 and x<=row-1 and y<=col-1:
                            if grid[x][y] == '1' and (x,y) not in visited:
                                visit.append((x,y))
                
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1' and (i,j) not in visited:
                    bfs(i,j)
                    island += 1
                    
        return island
        