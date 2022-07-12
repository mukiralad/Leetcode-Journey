# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        
        arr=[]
        
        def inorder(root):
            
            if root is None:
                return []
            
            return inorder(root.left)+[root.val]+inorder(root.right)
        
        x=inorder(root)
        
        y=Counter(x)
        
        maxi=0
        res=[]
        
        for i in y:
            if(y[i]>maxi):
                maxi=y[i]
        
        for i in y:
            if(y[i]==maxi):
                res.append(i)
        
        return res