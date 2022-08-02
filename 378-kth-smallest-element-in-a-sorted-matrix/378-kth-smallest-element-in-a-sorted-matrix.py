class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        x=[]
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                x.append(matrix[i][j])
        
        x=sorted(x)
        return x[k-1]
        