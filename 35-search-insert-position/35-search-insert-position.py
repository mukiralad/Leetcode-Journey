class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        if(target in nums):
            start=0
            end=len(nums)-1
            mid=0
        
            while(start<=end):
            
                mid=(start+end)//2
            
                if(nums[mid]==target):
                    return mid
                elif(nums[mid]>target):
                    end=mid-1
                else:
                    start=mid+1
        
            return -1
        else:
            
            d=min(nums, key=lambda x:abs(x-target))
            print(d)
            e=nums.index(d)
            
            if(target>d):
                return(e+1) 
            else:
                return(e)
            
            
             
            
                
        
            
            
        
        
      
    
        
    
    
        