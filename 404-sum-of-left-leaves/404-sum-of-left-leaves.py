# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        if root is None:
            return 0
        
        temp=0
        
        if root.left and not root.left.left and not root.left.right:
            temp=temp+root.left.val
        
        return temp+self.sumOfLeftLeaves(root.left)+self.sumOfLeftLeaves(root.right)
        
        
        
        