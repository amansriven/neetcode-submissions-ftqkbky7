import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_prod = 1
        left = []
        for n in nums:
            left.append(left_prod)
            left_prod *= n

        right_prod = 1
        right = [1] * (len(nums) + 1)
        for i in range(len(nums)-1, -1, -1):
            right[i] = right_prod
            right_prod *= nums[i]
        
        res = []
        for i in range(len(nums)):
            if i == 0:
                res.append(right[i])
                continue
            if i == len(nums) - 1:
                res.append(left[i])
                continue
            res.append(left[i]*right[i])
        return res
        
