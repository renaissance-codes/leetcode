/**
    最长回文子串
*/

class Solution {
public:
    string longestPalindrome(string s) {
        int size = s.size();
        if(size<2){
            return s;
        }
        vector<vector<int> > newOne(size, vector<int>(size, 0));
        int maxv = 1;
        int start = 0;

        for(int i=0; i<size; i++){
            newOne[i][i] = 1;
            if(i+1<size){
                if(s[i]==s[i+1]){
                    newOne[i][i+1] = 1;
                    maxv = 2;
                    start = i;
                }
            }
        }

        for(int i=2; i<size; i++){
            for(int j=0; j<size-i; j++){
                if(s[j]==s[j+i] && newOne[j+1][j+i-1]){
                    newOne[j][j+i] = 1;
                    if((i+1)>maxv){
                        start = j;
                        maxv = i+1;
                    }
                }
            }

        }
        string res(maxv, ' ');
        for(int i=start; i<start+maxv; i++){
            res[i-start] = s[i];
        }
        return res;
    }
};