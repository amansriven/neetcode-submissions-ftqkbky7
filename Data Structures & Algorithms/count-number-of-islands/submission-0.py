from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        vis = set()
        islands = 0

        def traverse(r, c):
            if min(r, c) < 0 or r == len(grid) or c == len(grid[0]) or grid[r][c] == "0" or (r, c) in vis:
                return
            
            vis.add((r, c))
            traverse(r-1, c)
            traverse(r, c-1)
            traverse(r, c+1)
            traverse(r+1, c)

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and (r, c) not in vis:
                    islands += 1
                    traverse(r, c)
        return islands



