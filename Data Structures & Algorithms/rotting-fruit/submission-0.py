class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        q = deque()
        mins = 0
        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1

        while q and fresh > 0:
            level_size = len(q)

            for i in range(level_size):
                r, c = q.popleft()
                directions = [[-1, 0], [0, -1], [0, 1], [1, 0]]

                for dr, dc in directions:
                    rx, cx = dr + r, dc + c
                    if rx in range(rows) and cx in range(cols) and grid[rx][cx] == 1:
                        grid[rx][cx] = 2
                        q.append((rx, cx))
                        fresh -= 1

            mins += 1
        
        return mins if fresh == 0 else -1