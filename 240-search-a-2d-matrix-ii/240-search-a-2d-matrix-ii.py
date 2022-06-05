class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        flag=0
        for i in range(len(matrix)):
            
            for j in range(len(matrix[0])):
                
                if(matrix[i][j]==target):
                    flag=1
        
        if(flag==1):
            return True
        else:
            return False
        