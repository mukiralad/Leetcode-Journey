# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

    
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        
        val=[]
        
        def inorder(node:TreeNode):
            
            if(node is None):
                return
            
            inorder(node.left)
            val.append(node.val)
            inorder(node.right)
        
        
        inorder(root)
        root=TreeNode()
        result=root
        
        for i in val:
            
            node=TreeNode(i)
            result.right=node
            result=result.right
        
        return root.right
            
        
        
        
        
        