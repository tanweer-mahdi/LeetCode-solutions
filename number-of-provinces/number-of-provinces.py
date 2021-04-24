class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        ## Using BFS
        visited = set()
        provinces = 0
        
        def bfs(row):
            visited.add(row)
            for col in range(len(isConnected)):
                if isConnected[row][col] == 1 and col not in visited:
                    bfs(col)
        
        for row in range(len(isConnected)):
            if row not in visited:
                bfs(row)
                provinces += 1
                
        return provinces
        
        