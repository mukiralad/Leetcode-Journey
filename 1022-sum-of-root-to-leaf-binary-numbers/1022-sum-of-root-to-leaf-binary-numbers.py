# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root,string=""):
            
            if root is None:
                return []
            
            if not root.left and not root.right:
                return [string+str(root.val)]
            
            return dfs(root.left,string+str(root.val))+dfs(root.right,string+str(root.val))
        
        x=dfs(root)
        print(x)
        
        ans=[]
        for i in x:
            ans.append(int(i))
        print(ans)
        num=[]
        for i in ans:
            i=str(i)
            num.append(int(i,2))
        
        return sum(num)
        