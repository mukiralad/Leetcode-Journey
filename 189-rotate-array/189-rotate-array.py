class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        if(len(nums)==0):
            return
        
        k=k%len(nums)
        
        rem=len(nums)-k
        
        nums[k:],nums[:k]=nums[:rem],nums[rem:]
        
            
            
        
        