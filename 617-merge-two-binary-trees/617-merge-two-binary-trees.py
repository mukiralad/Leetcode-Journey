# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def solve(root1,root2):
        if(root1 is None):
            return root2
        if(root2 is None):
            return root1
        
        root1.val=root1.val+root2.val
        
        root1.left= solve(root1.left,root2.left)
        root1.right= solve(root1.right,root2.right)
        
        return root1
    
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        x= solve(root1,root2)
        
        return x
        
        
    
        