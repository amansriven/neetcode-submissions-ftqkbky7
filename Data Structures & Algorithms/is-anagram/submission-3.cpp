class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()) return false;
        unordered_map<char, int> abc;
        for (int i = 0; i < s.length(); i++) {
            abc[s[i]]++;
            abc[t[i]]--;
        }
        for (auto letter : abc) {
            if (letter.second != 0)
                return false;
        }
        return true;
        }
};
