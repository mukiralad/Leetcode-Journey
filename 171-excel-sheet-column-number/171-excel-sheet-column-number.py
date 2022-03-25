class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        
        
        ans=0
        pow=0
        
        for char in reversed(columnTitle):
            
            digit=ord(char)-64
            
            ans+=digit*26**pow
            
            pow+=1
            
            
        return ans
        