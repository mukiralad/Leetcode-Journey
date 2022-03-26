class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        nums=set(nums)
        
        if(len(nums)<3):
            return max(nums)
        else:
            
            for i in range(2):
            
                s=max(nums)
                nums.remove(s)
        
            return max(nums)
        
        
        
       
    
    
    
       
    
        
        
        