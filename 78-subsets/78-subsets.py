class Solution:
    
    def search(self, nums, i, res):
        self.res.append(list(res))
        for j in range(i, len(nums)):
            res.append(nums[j])
            self.search(nums, j+1, res)
            res.pop()
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.search(nums, 0, [])
        return self.res