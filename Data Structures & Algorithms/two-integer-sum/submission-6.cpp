class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> vals;
        for (int i = 0; i < nums.size(); i++) {
            if (i == 0) {
                vals[nums[i]] = 0;
                continue;
            }
            int comp = target - nums[i];
            if (vals.find(comp) != vals.end()) {
                return {vals[comp], i};
            }
            vals[nums[i]] = i;
        }
        return {};
    }
};
