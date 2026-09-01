# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def helper(self, root: Optional[TreeNode], low: int, high: int) -> bool:
        if root == None: return True

        if root.val > low and root.val < high and self.helper(root.left, low, root.val) and self.helper(root.right, root.val, high):
            return True
        else:
            return False
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None: return True

        return self.helper(root, -1000000000, 1000000000)



