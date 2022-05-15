class Solution:
    def countPrimes(self, n: int) -> int:
        
        if(n==2):
            return 0
        if(n==0):
            return 0
        if(n==1):
            return 0
        
        x=[]
        prime=[True for i in range(n+1)]
        
        p=2
        
        while(p*p<=n):
            
            if(prime[p]==True):
                
                for i in range(p*p,n+1,p):
                    
                    prime[i]=False
            
            p+=1
        
        for i in range(2,n):
            if(prime[i]):
                
                x.append(i)
        
        print(x)
        return len(x)
            
        
        
        
        
        
        