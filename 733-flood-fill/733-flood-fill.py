def fill(image,sr,sc,initial,color):
        
        if sr<0 or sr>=len(image) or sc<0 or sc>=len(image[0]) or image[sr][sc]!=initial:
            return 
        
        image[sr][sc]=color
        
        fill(image,sr+1,sc,initial,color)
        fill(image,sr-1,sc,initial,color)
        fill(image,sr,sc+1,initial,color)
        fill(image,sr,sc-1,initial,color)
    
        
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        if (image is None or image[sr][sc]==color):
            return image
        
        fill(image,sr,sc,image[sr][sc],color)
        return image
        
    
    