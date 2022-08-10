class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        x=""
        for i in digits:
            x+=str(i)
        print(x)
        ans=str(int(x)+1)
        res=[]
        for i in ans:
            res.append(int(i))
        
        return res
        