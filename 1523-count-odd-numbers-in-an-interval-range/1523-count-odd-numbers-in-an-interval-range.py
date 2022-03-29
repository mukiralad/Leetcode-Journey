class Solution:
    def countOdds(self, low: int, high: int) -> int:
        
        total=high-low
        
        if(low%2==0 and high%2==0):
            return total//2
        else:
            return total//2+1
        