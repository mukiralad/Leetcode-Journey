class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        x=[]
        y=Counter(nums)
        for i in range(1,len(nums)+1):
            if(i not in y):
                x.append(i)
        
        return x
        