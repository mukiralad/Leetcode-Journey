def check(n):
        if(n==0):
            return False
        
        elif(n%3==0):
            return check(n//3)
        
        if(n==1):
            return True
        else:
            return False

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
        if(check(n)):
            return True
        else:
            return False
        