class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        l = 0
        end = len(nums) - 1
        while l <= end:
            mid = (l + end)// 2
            if nums[mid] == target:
                last = mid
                first = mid
                while last != len(nums) - 1 and nums[last+1] == nums[mid]:
                    last += 1
                while first != 0 and nums[first - 1] == nums[mid]:
                    first -= 1
                return [first, last]
            elif nums[mid] > target:
                end = mid - 1
            else:
                l = mid + 1
        return [-1,-1]
        
       
                    
       