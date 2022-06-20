class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        x=Counter(s)
        print(x)
        
        for i in range(len(s)):
            if(s[i] in x and x[s[i]]==1):
                return i
        
        return -1
        
        
        
        
                
               
                
        