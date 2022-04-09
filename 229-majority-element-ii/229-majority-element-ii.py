class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        n=len(nums)
        x=Counter(nums)
        
        ans=[]
        
        if(n==1):
            return nums
        
        for i in x:
            if(x[i]>math.floor(n/3)):
                ans.append(i)
        
                
        return(ans)
                
        