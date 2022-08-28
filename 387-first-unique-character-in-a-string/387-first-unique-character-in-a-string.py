class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        x=Counter(s)
        for i in x:
            if x[i]==1:
                return s.index(i)
            
        return -1