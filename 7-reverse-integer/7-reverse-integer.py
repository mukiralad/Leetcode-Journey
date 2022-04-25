class Solution:
    def reverse(self, x: int) -> int:
        
        if(x==0):
            return 0
        d=str(x)
        
        s=''
        
        if(x>0):
            ans=d[::-1]
            if(-2**31<=int(ans)<=2**31-1):
                return ans.lstrip('0')
            else:
                return 0
        else:
            for i in range(1,len(d)):
                s+=d[i]
                
            anss=s[::-1]
            
            if(-2**31<=int(anss)<=2**31-1):
                
                return('-' + anss.lstrip('0'))
            else:
                return 0
                
    
        