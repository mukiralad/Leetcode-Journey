class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        
        y=[]
        while(n>0):
            x=n%10
            y.append(x)
            n=n//10
        
        z=y[::-1]
        
        prod=1
        
        for i in z:
            prod=prod*i
        
        
        return (prod-sum(z))
        
        
            
            
        