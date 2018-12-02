// The naive solution is to sort the list O(nlogn) and then just
// take the Kth largest element O(1). Let's try to do better.


// Solution 1: Build a max heap and pop off the max element k times
// Runtime: O(n) to build the heap + O(klogn) to pop off the max element
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

// Solution 2: Use quick select, which has average case complexity O(n) but worst
// case O(n^2)