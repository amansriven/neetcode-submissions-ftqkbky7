class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = []
        for x in nums:
            if x not in hashmap:
                hashmap.append(x)
            elif x in hashmap:
                return True
        return False
        
        