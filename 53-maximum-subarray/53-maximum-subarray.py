class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        currsum=0
        maxsum=nums[0]
        
        n=len(nums)
        
        for i in range(n):
            currsum=currsum+nums[i]
            
            if(currsum>maxsum):
                maxsum=currsum
            if(currsum<0):
                currsum=0
        
        return maxsum
            
                
            
                
                
                
                
                
        