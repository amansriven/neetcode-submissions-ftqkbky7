class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

# -4, -1, -1, 0, 1, 2
        for i in range(len(nums)):
            # skip duplicate vals for first triplet
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = len(nums) - 1

            while l < r:
                curr = nums[l] + nums[i] + nums[r]
                
                if curr > 0:
                    r -= 1
                elif curr < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])

                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l, r = l + 1, r - 1
        
        return res
            
