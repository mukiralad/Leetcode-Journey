class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        Dict={}
        
        for i in arr:
            if(i in Dict):
                Dict[i]+=1
            else:
                Dict[i]=1
                
        print(Dict)
        
        x=[]
        
        for i in Dict:
            x.append(Dict[i])
        
        f=len(x)
        
        y=set(x)
        
        e=len(y)
        
        if(f==e):
            return True
        else:
            return False
        
        
            
                