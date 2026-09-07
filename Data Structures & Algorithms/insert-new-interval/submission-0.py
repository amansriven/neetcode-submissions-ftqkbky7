class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i, curr in enumerate(intervals):
            # ends before
            if newInterval[1] < curr[0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > curr[1]:
                res.append(curr)
            else:
                newInterval[0] = min(newInterval[0], curr[0])
                newInterval[1] = max(newInterval[1], curr[1])
        
        res.append(newInterval)

        return res