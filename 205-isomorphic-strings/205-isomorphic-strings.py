class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        x=set(zip(s,t))
        print(x)
        
        y=len(set(s))
        print(y)
        
        z=len(set(t))
        print(z)
        
        if(y==z==len(x)):
            return True
        else:
            return False
        
                
        
            
        