class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        x={}
        y={}
        
        for c1,c2 in zip(s,t):
            
            if(c1 not in x) and (c2 not in y):
                x[c1]=c2
                y[c2]=c1
                
            
            elif(x.get(c1)!=c2 or y.get(c2)!=c1):
                return False
            
        return True
        
        
                
        
            
        