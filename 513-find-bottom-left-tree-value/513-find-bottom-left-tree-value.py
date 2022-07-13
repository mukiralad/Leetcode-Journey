# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        
        ans=[]
        
        def dfs(root,depth):
            
            if root is None:
                return
            if depth>=len(ans):
                ans.append([])
                
            ans[depth].append(root.val)
            dfs(root.left,depth+1)
            dfs(root.right,depth+1)
        
        dfs(root,0)
        return(ans[-1][0])
        