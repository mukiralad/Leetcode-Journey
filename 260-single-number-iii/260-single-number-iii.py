class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        
        if(len(nums)==2):
            return nums
        
        x=Counter(nums)
        print(x)
        
        res=[]
        
        for i in x:
            if(x[i]!=2):
                res.append(i)
        
        return res
            
        