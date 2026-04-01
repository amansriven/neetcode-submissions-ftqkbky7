class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> vals;
        vals.reserve(nums.size());

        for (int i = 0; i < nums.size(); i++) {
            int complement = target - nums[i];

            auto it = vals.find(complement);
            if (it != vals.end()) {
                return {it->second, i};
            }

            vals[nums[i]] = i;
        }
        return {};
    }
};