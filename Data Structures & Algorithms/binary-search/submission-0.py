class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        mid = (high - low) // 2
        while (low <= high):
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            mid = low + ((high - low) // 2)
        return -1