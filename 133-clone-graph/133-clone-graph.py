"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        old={}
        
        def dfs(node):
            if node in old:
                return old[node]
            else:
                copy=Node(node.val)
                old[node]=copy
            
            for i in node.neighbors:
                copy.neighbors.append(dfs(i))
            return copy
        
       
        return dfs(node) if node else None
                
                
        