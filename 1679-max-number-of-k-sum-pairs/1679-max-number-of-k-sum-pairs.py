class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        start=0
        end=len(nums)-1
        
        count=0
        
        while(start<end):
            
            curr=nums[start]+nums[end]
            
            if(curr==k):
                count+=1
                start+=1
                end-=1
            
            elif(curr<k):
                start+=1
            else:
                end-=1
        
        return count
        
        
        