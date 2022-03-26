class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        i=1
        
        while(i*i<=num):
            ans=i*i
            i=i+1
            
        if ans==num:
            return True
        else:
            return False
        