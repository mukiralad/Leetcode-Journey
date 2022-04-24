class Solution:
    def numSub(self, s: str) -> int:
        
        count,ans=0,0
        
        for i in range(len(s)):
            
            if(s[i]=='0'):
                count=0
            else:
                count+=1
                ans+=count
        
        return ans%((10**9)+7)
        
        
        