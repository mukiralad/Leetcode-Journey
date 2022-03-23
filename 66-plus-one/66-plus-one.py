class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = int("".join(map(str, digits)))
        
        x=res+1
        
        print(x)
        
        z=[]
        
        while(x>0):
            k=x%10
            z.append(k)
            x=x//10
        
        return z[::-1]
            

        
        
        
        