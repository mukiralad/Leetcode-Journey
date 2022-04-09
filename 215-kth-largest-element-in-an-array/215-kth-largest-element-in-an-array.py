class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        nums=sorted(nums)
        print(nums)
        
        x=sorted(nums,reverse=True)
        
        return(x[k-1])
        
          
            
       