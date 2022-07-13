# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        ans=[]
        
        def pre(root):
            
            if root is None:
                return []
            
            if root.left is None and root.right is None:
                ans.append(root.val)
            pre(root.left)
            pre(root.right)
        
        pre(root1)
        print(ans)
        sex=[]
        def pre(root):
            
            if root is None:
                return []
            
            if root.left is None and root.right is None:
                sex.append(root.val)
            
            pre(root.left)
            pre(root.right)
        
        pre(root2)
        print(sex)
        
        if(ans==sex):
            return True
        else:
            return False
        
     
            
        