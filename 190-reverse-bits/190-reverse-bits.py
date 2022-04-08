def reverse(n):
    return n[::-1]

class Solution:
    def reverseBits(self, n: int) -> int:
      
        x='{:032b}'.format(n)
        
        x=str(x)
        y=reverse(x)
        
        res=int(y,2)
        
        return(res)
        
        
        