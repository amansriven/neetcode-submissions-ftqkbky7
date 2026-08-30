class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0
        for n in num_set:
            if n-1 not in num_set:
                curr_seq = 1
                nextval = n+1
                while nextval in num_set:
                    curr_seq += 1
                    nextval += 1
                longest = max(longest, curr_seq)
        return longest