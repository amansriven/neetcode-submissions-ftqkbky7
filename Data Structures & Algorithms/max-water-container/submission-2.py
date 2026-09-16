class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxA = -float('inf')

        while l < r:
            currA = min(heights[l], heights[r]) * (r - l)
            maxA = max(currA, maxA)

            if heights[r] > heights[l]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            else:
                l, r = l + 1, r - 1
                        
        return maxA