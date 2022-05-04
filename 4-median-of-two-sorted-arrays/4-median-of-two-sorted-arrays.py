class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        x=nums1+nums2
        x.sort()
        
        
        n=len(x)
        
        if(n%2!=0):
            
            m = int((len(x)+1)/2 - 1)
            return x[m]
        
        else:
            
            m1=int(len(x)/2 -1)
            m2=int(len(x)/2)
            
            return (x[m1]+x[m2])/2
        
    
        