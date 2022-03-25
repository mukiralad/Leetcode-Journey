# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        stack=[root]
        
        res=[]
        
        if(root is None):
            return None
        while(stack!=[]):
            
            root=stack.pop()
            res.append(root.val)
            
            if(root.right is not None):
                stack.append(root.right)
            
            if(root.left is not None):
                stack.append(root.left)
            
            
        return res
            
            
            
        
        
        