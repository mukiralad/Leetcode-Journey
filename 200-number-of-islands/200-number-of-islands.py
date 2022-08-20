class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        count=0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                if(grid[i][j]=='1'):
                    
                    self.dfs(i,j,grid)
                    count+=1
        
        return count
    
    def dfs(self,a,b,grid):
        
        if a<0 or a>=len(grid) or b<0 or b>=len(grid[0]):
            return
        
        if(grid[a][b]=='1'):
            grid[a][b]='-1'
            self.dfs(a+1,b,grid)
            self.dfs(a-1,b,grid)
            self.dfs(a,b+1,grid)
            self.dfs(a,b-1,grid)
    
        