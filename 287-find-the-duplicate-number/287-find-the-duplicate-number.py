class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        x=Counter(nums)
        
        for i in x:
            
            if(x[i]>1):
                return i
        
        