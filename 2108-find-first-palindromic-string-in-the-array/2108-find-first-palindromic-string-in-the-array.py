def pali(x):
        if(x==x[::-1]):
            return True
        else:
            return False
class Solution:
    
    def firstPalindrome(self, words: List[str]) -> str:
        
        for i in words:
            if(pali(i)):
                return i
        
        return ""
        
        
            
            
        