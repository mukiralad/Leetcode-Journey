class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        
        x=[]
        
        for i in edges:
            x.append(i[0])
            x.append(i[1])
        
        print(x)
        
        ans=Counter(x)
        
        z=[]
        
        print(ans)
        
        res=0
        maxi=0
        for i in ans:
            if(ans[i]>maxi):
                maxi=i
                res=ans[i]
                
        return maxi
        
    
        

        