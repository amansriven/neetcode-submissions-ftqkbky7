
class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "%" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            size_str = ""
            while(s[i] != '%'):
                size_str += s[i]
                i += 1
            size = int(size_str)
            i += 1
            res.append(s[i:i + size])
            i += size
        return res
