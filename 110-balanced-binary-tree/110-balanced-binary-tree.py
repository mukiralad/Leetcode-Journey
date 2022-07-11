# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        if(root is None):
            return True
        
        left=self.getMaxDepth(root.left)
        right=self.getMaxDepth(root.right)
        
        
        if(left-right<=1 and left-right>=-1):
            if(self.isBalanced(root.left) and self.isBalanced(root.right)):
                
                return True
            else:
                return False
        else:
            return False
        
    def getMaxDepth(self,root):
        if root is None:
            return 0
        
        left=self.getMaxDepth(root.left)
        right=self.getMaxDepth(root.right)
        
        return max(left,right)+1
        
        
        
       