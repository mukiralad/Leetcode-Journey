class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        
        
        Dict={}
        for i in range(len(indices)):
            Dict[indices[i]]=s[i]
        
        
        
        
        ss=""
        
        for i in range(len(s)):
            ss=ss+Dict.get(i)
            
        return ss
        
        
            
            
            