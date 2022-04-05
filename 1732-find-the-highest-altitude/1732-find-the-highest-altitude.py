class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
        x=[]
        x.append(0)
        count=0
        
        
        for i in range(len(gain)):
            
            
            count=count+gain[i]
            x.append(count)
            
        return max(x)
            
            
            
            
        
        
        
        
        