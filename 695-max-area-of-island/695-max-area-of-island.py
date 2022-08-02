class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        r=len(grid)
        c=len(grid[0])
        
        visit=set()
        
        def dfs(r,c):
            
            if r<0 or r>=len(grid) or c<0 or c>=len(grid[0]) or grid[r][c]==0 or (r,c) in visit:
                return 0
            visit.add((r,c))
            return 1+dfs(r+1,c)+dfs(r-1,c)+dfs(r,c+1)+dfs(r,c-1)
        
        area=0
        for i in range(r):
            for j in range(c):
                x=dfs(i,j)
                area=max(area,x)
        
        return area
                
                    
        
        
        
        
       
        
                    
                
        