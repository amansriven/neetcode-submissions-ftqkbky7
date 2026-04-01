class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> mp;
        vector<vector<string>> result;
        for (auto str : strs) {
            int abc[26] = {0};
            for (char c : str) {
                abc[c - 'a']++;
            }
            string key;
            for (int x : abc) {
                key += to_string(x) + ".";
            }
            mp[key].push_back(str);
        }
        for (auto pair : mp) {
            result.push_back(pair.second);
        }
        return result;
    }
};