class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        pos=[]
        neg=[]
        for i in nums:
            if(i>0):
                pos.append(i)
            else:
                neg.append(i)
        arr=[]
        for i in range(len(nums)//2):
            arr.append(pos[i])
            arr.append(neg[i])
        
        return arr
        