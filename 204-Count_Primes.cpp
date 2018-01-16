class Solution {
public:
    bool isPrime(int n){
        if(n==2)
            return true;
        for(int i = 2; i * i <= n ; i++) {
            if(n%i == 0){
                return false;
            }
        }
        return true;
    }
    int countPrimes(int n) {
        int count = 0;
        for(int i = 2;i < n; i++){
            if(isPrime(i)) {
                count++;
            }
        }
        return count;
    }
};
