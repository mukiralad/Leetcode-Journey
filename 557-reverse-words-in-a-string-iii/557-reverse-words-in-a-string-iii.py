def reverse(string):
    string = string[::-1]
    return string

class Solution:
    def reverseWords(self, s: str) -> str:
        
        s=s.split(' ')
        
        
        
        x=''
        
        for i in s:
            l=reverse(i)
            x+=l
            x+=' '
            
            
        return x.rstrip()
        