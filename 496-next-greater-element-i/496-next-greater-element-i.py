class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        res=[]
        
        for i in nums1:
            
            if(i>=max(nums2[nums2.index(i):])):
                res+=[-1]
                
            else:
                
                for j in nums2[nums2.index(i):]:
                    
                    if(j>i):
                        res+=[j]
                        break
        
        return res
            
        
        
            
            
           
            
            
                