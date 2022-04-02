class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        Dict={}
        
        for i in range(len(nums)):
            
            if target-nums[i] in Dict:
                return[Dict[target-nums[i]],i]
                
            Dict[nums[i]]=i
                
        