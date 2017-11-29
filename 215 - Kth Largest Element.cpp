// Builds a max heap and pops off the max element k times
// Runtime: O(n) to build heap + O(klogn) to pop off the max element
class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        make_heap(nums.begin(), nums.end());
        for(int i = 0; i < k-1; i++) {
            pop_heap(nums.begin(), nums.end());
            nums.pop_back();
        }
        return nums.front();
    }
};

// The naive solution is to sort the list and then just take the Kth largest element O(nlogn)
// The best solution is to use quick select, which has average case complexity O(n)