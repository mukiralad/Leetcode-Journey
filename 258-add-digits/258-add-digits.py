class Solution:
    def addDigits(self, num: int) -> int:
        
        ans=0 
        
        while(num>0):
            
            x=num%10
            ans=ans+x
            num=num//10
            
        if(ans>9):
            return self.addDigits(ans)
        else:
            return ans
            
            
        
        
            
            
        