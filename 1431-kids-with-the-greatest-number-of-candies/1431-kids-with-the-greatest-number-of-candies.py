class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        n=max(candies)
        x=[]
        
        for i in range(len(candies)):
            if(candies[i]+extraCandies>=max(candies)):
                x.append(True)
            else:
                x.append(False)
        
        return x
                
        