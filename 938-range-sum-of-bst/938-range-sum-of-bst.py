# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def solve(root,s,low,high):
    
    
    if(root is None):
        return
    else:
        if(low<=root.val<=high):
            
            s.append(root.val)
        
        solve(root.left,s,low,high)
        solve(root.right,s,low,high)
            
            
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        s=[]
        
        solve(root,s,low,high)
        
        return sum(s)
    
        
        
        
            
                
        