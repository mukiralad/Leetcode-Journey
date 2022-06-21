class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        lsum=0
        rsum=sum(nums)
        
        for i in range(len(nums)):
            rsum=rsum-nums[i]
            
            if(rsum==lsum):
                return i
            else:
                lsum=lsum+nums[i]
        
        return -1