# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        
        arr=[]
        
        def order(root):
            
            if root is None:
                return []
            
            return order(root.left)+[root.val]+order(root.right)
        
        x=order(root)
        minn=9999
        
        for i in range(1,len(x)):
            if(abs(x[i]-x[i-1])<minn):
                minn=abs(x[i]-x[i-1])
                
        return minn
        