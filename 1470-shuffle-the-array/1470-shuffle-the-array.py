class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        
        z=[]
        for i in range(n):
                z.extend((nums[i],nums[i+n]))
                
        return z
                
        
        
       
                           
            
        
        
        
        
        
        