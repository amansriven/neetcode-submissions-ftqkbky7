class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prev, removed = -float('inf'), 0
        for curr in intervals:
            if prev > curr[0]:
                removed += 1
                if prev < curr[1]:
                    continue
            prev = curr[1]
        return removed