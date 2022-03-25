class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        Dict={}
        
        for i in nums:
            if(i in Dict):
                Dict[i]=Dict[i]+1
            else:
                Dict[i]=1
                
        
        print(Dict)
        
        for i in Dict:
            if(Dict[i]>=2):
                return True
         
            
            