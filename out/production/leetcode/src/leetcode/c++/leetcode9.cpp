class Solution {
public:
    bool isPalindrome(int x) {
        if(x<0){
            return false;
        }
        int xi = x;
        int v = 0;
        while(xi){
            if(v>INT_MAX/10||(v==INT_MAX&&xi%10>7)){
                return false;
            }
            v = 10*v+xi%10;
            xi /= 10;
        }

        return v==x;
    }
};