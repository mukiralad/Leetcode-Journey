class Solution:
    def isValid(self, s: str) -> bool:
        
        for i in range(len(s)):
            
            if("()" in s):
                s=s.replace("()","")
            
            if "[]" in s:
                s=s.replace("[]","")
            
            if("{}" in s):
                s=s.replace("{}","")
                
        
        if(s==""):
            return True
        else:
            return False
        