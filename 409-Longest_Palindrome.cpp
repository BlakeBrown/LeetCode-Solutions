class Solution {
public:
    int longestPalindrome(string s) {
        int a[256];
        int flag = 0;
        for(int i = 0; i < 256; i++) {
            a[i] = 0;
        }
        for(int i = 0; i < s.size();i++) {
            a[s[i]]++;
        }
        int count = 0;
        int max = 0;
        for(int i = 0; i < 256 ; i++) {
             count = count + a[i] - a[i]%2;
             a[i] = a[i]%2;    
        }
        for(int i = 0; i < 256 ; i++) {
            if(a[i] == 1) {
                count+=1;
                break;
            }
        }
        return count;
    }
};
