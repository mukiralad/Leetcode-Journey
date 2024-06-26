# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def last(l):
            return l[-1]
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
        
        print(ans)
        fun=[]
        for i in range(len(ans)):
            fun.append(last(ans[i]))
        
        return fun
        