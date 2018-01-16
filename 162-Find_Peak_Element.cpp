class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        return peak(0,nums.size() - 1,nums);
    }
public:
    int peak(int l, int n, vector<int>&nums) {
        l = 0;
        int r = n;
        while (l < r) {
            int mid = (l + r) / 2;
            if (nums[mid] > nums[mid + 1])
                r = mid;
            else
                l = mid + 1;
        }
        return l;
    }
};
