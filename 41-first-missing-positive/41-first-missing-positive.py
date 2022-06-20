class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        x=Counter(nums)
        for i in range(1,len(nums)+2):
            
            if(i not in x):
                return i
        
        return nums[-1]+1
          
        