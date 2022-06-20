class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        x=set()
        
        y=Counter(nums)
        
        for i in nums:
            
            if (i in y and y[i]==2):
                x.add(i)
        
        return x
        