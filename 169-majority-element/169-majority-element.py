class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        n=len(nums)
        
        Dict={}
        
        for i in nums:
            if(i in Dict):
                Dict[i]=Dict[i]+1
            else:
                Dict[i]=1
        
        
        for i in Dict:
            if(Dict[i]>math.floor(n/2)):
                return i
                
        