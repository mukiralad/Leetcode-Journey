class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        
        ar=[]
        
        ar.append(first)
        
        x=first
        for i in encoded:
            x=i^x
            ar.append(x)
        
        return ar
            
        
        