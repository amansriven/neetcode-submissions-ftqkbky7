from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        vis = set()
        islands = 0
        rows = len(grid)
        cols = len(grid[0])

        def bfs(r, c):
            queue = deque()
            queue.append((r, c))
            vis.add((r, c))

            while queue:
                row, col = queue.popleft()
                
                directions = [[-1, 0], [0, -1], [0, 1], [1, 0]]
                for dr, dc in directions:
                    rx, cx = dr + row, dc + col
                    if rx in range(rows) and cx in range(cols) and grid[rx][cx] == "1" and (rx,cx) not in vis:
                        vis.add((rx,cx))
                        queue.append((rx,cx))


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in vis:
                    islands += 1
                    bfs(r, c)
        return islands
