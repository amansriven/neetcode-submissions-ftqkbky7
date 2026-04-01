class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> vals;
        for (int i = 0; i < nums.size(); i++) {
            if (i == 0) {
                vals[nums[i]] = 0;
                continue;
            }
            int complement = target - nums[i];
            if (vals.find(complement) != vals.end()) {
                return {vals[complement], i};
            }
            vals[nums[i]] = i;
        }
        return {};
    }
};
