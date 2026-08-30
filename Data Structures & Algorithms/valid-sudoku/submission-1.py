class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            seen = set()
            for s in board[i]:
                if s != ".":
                    if s in seen:
                        return False
                    seen.add(s)

        for i in range(9):
            seen = set()
            for j in range(9):
                s = board[j][i]
                if s != ".":
                    if s in seen:
                        return False
                    seen.add(s)
        
        for i in range(9):
            seen = set()
            row = (i // 3) * 3
            col = (i % 3) * 3
            for r in range(3):
                for c in range(3):
                    s = board[row + r][col + c]
                    if s == ".":
                        continue
                    if s in seen:
                        return False
                    seen.add(s)

        return True