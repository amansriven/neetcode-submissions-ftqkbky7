# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None: return []

        queue = deque()
        queue.append(root)
        res = []

        while queue:
            level_size = len(queue)
            curr_lvl = []
            
            for i in range(level_size):
                curr = queue.popleft()
                curr_lvl.append(curr.val)
                if curr.left: queue.append(curr.left)
                if curr.right: queue.append(curr.right)
            res.append(curr_lvl)

        return res
