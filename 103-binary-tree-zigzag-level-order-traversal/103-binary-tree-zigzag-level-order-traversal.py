# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
   
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def reverse(li):
                return li[::-1]
        
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
        
        fin=[]
        print(ans)
        for i in range(len(ans)):
            if(i%2!=0):
                fin.append(reverse(ans[i]))
            else:
                fin.append(ans[i])
        
        return fin
                
        