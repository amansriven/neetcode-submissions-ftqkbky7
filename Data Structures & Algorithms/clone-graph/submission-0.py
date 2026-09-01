"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        clones = {}

        def dfs(old):
            if old in clones:
                return clones[old]
            if old is None:
                return
            
            new = Node(old.val)
            clones[old] = new

            for n in old.neighbors:
                new.neighbors.append(dfs(n))
            return new
        
        res = dfs(node)
        return res
