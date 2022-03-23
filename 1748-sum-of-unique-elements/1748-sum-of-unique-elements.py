class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        
        z=[]
        for i in nums:
            if(nums.count(i)>1):
                continue
            else:
                z.append(i)
        
        return sum(z)
                