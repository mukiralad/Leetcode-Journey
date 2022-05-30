def insert(nums,temp):
        
        if((len(nums)==0) or (nums[len(nums)-1]<=temp)):
            
            nums.append(temp)
            return
        
        val=nums[len(nums)-1]
        
        nums.pop()
        
        insert(nums,temp)
        
        nums.append(val)
        
        
class Solution:    
    def sortArray(self, nums: List[int]) -> List[int]:
        
        temp=nums.pop()
        
        nums.sort()
        
        print(nums)
        
        insert(nums,temp)
        
        return nums
        
       
    
        
        
        