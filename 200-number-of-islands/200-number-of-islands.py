class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        islands=0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j]=="1"):
                    islands+=1
                    self.dfs(i,j,grid)
        
        return islands
        
    
    def dfs(self,r,c,grid):
        
        if r<0 or r>=len(grid) or c<0 or c>=len(grid[0]):
            return
        
        if(grid[r][c]=="1"):
            grid[r][c]="0"
            self.dfs(r+1,c,grid)
            self.dfs(r-1,c,grid)
            self.dfs(r,c+1,grid)
            self.dfs(r,c-1,grid)
            
            