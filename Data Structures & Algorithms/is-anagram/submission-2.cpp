class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()) return false;
        unordered_map<char, int> count1;
        unordered_map<char, int> count2;
        for (int i = 0; i < s.length(); i++) {
            if (count1.find(s[i]) == count1.end())
                count1[s[i]] = 1;
            else
                count1[s[i]] += 1;
            if (count2.find(t[i]) == count2.end())
                count2[t[i]] = 1;
            else
                count2[t[i]] += 1;
            
        }
        if (count1 == count2) return true;
        return false;
    }
};
