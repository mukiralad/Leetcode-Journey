class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        
        lsum=0
        rsum=sum(nums)
        
        for i in range(len(nums)):
            
            rsum-=nums[i]
            
            if(rsum==lsum):
                return i
            else:
                
                lsum+=nums[i]
            
        return -1