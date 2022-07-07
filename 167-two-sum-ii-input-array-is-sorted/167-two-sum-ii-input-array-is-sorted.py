class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        Dict={}
        
        for i in range(len(numbers)):
            
            if target-numbers[i] in Dict:
                
                return [Dict[target-numbers[i]]+1,i+1]
            
            Dict[numbers[i]]=i
        
        