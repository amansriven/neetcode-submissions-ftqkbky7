class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mpp = {}

        for word in strs:
            abc = [0] * 26

            for char in word:
                abc[ord(char) - ord('a')] += 1

            key = tuple(abc)

            if key not in mpp:
                mpp[key] = [word]
            else:
                mpp[key].append(word)

        return list(mpp.values())