class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mpp = {}
        for word in strs:
            abc = [0]*26
            key = ""
            for char in word:
                abc[ord(char) - ord('a')] += 1
            for num in abc:
                key += str(num) + "."
            if key not in mpp:
                mpp[key] = [word]
            else:
                mpp[key].append(word)
        result = []
        for key, value in mpp.items():
            result.append(value)
        return result