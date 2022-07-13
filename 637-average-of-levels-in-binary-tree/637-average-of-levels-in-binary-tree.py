# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        ans=[]
        
        def dfs(root,depth):
            
            if root is None:
                return 
            
            if(depth>=len(ans)):
                ans.append([])
                
            ans[depth].append(root.val)
            dfs(root.left,depth+1)
            dfs(root.right,depth+1)
        
        dfs(root,0)
        
        print(ans)
        
        res=[]
        for i in ans:
            res.append(sum(i)/len(i))
        
        
        return res
            
        