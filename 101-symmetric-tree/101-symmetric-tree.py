# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        return self.isSym(root.left,root.right)
    
    def isSym(self,Left,Right):
        
        if(Left is None and Right is None):
            
            return True
        
        if(Left is None or Right is None):
            return False
        
        if(Left.val!=Right.val):
            return False
        
        return self.isSym(Left.left,Right.right) and self.isSym(Left.right,Right.left)

        