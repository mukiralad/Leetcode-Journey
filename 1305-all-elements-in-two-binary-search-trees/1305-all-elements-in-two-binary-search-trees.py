# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        
        ans=[]
        
        def pre(root1):
            if root1 is None:
                return
            
            pre(root1.left)
            ans.append(root1.val)
            pre(root1.right)
        
        pre(root1)
        pre(root2)
        
        return sorted(ans)
    
            
        