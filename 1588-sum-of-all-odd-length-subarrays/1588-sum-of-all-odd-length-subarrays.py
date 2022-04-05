class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        
        lists=[[]]
        
        for i in range(len(arr)+1):
            for j in range(i):
                
                lists.append(arr[j:i])
        
        count=0
        
        for i in lists:
            if(len(i)%2!=0):
                
                count=count+sum(i)
        
        return count
                
        
        
        