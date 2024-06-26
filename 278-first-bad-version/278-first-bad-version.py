# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    
    def firstBadVersion(self, n: int) -> int:
        
        
        if(n==1):
            return 1
        
        start=0
        end=n
        
        while(start<=end):
            
            mid=(start+end)//2
            
            if(isBadVersion(mid)):
                if(isBadVersion(mid-1)):
                    end=mid-1
                else:
                    return mid
            else:
                start=mid+1
            
        
            