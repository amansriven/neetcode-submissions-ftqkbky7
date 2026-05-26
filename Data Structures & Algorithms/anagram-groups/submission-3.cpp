class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> mp;
        for (string str : strs) {
            int abc[26] = {0};
            for (char c : str) {
                abc[c - 'a']++;
            }
            string key;
            for (int a : abc) {
                key += to_string(a) + ".";
            }
            mp[key].push_back(str);
        }
        vector<vector<string>> result;
        for (auto pair : mp) {
            result.push_back(pair.second);
        }
        return result;
    }
};