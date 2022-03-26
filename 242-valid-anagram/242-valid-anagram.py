class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        s=sorted(s)
        t=sorted(t)
        
        Dict={}
        Dictt={}
        
        for i in s:
            if(i in Dict):
                Dict[i]=Dict[i]+1
            else:
                Dict[i]=1
                
        for i in t:
            if(i in Dictt):
                Dictt[i]=Dictt[i]+1
            else:
                Dictt[i]=1
                
        
       
        
        if(Dict==Dictt):
            return True
        else:
            return False
    