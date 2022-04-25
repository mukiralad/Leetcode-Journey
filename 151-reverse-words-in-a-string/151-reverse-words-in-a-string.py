class Solution:
    def reverseWords(self, s: str) -> str:
        
        x=" ".join(s.split())
        
        
        s=x.split()
        
        s.reverse()
        
        ans=''
        
        for i in s:
            ans+=i
            ans+=' '
        return(ans.rstrip(' '))
        