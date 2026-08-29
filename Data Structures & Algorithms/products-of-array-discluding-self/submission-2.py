class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_prod = 1
        left = []
        for n in nums:
            left.append(left_prod)
            left_prod *= n

        right_prod = 1
        res = [1] * (len(nums))
        for i in range(len(nums)-1, -1, -1):
            res[i] = (left[i]*right_prod)
            right_prod *= nums[i]

        return res
        
