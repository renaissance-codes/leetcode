


class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int len = s.length();
        map<char, int> vmap;
        int ans = 0;
        int start = -1;
        for(int i=0; i<len; i++){
            if(vmap.count(s[i]) and vmap[s[i]] !=-1){
                int nstart = vmap[s[i]];
                for(int j=start+1; j<=vmap[s[i]]; j++){
                    vmap[s[j]] = -1;
                }
                start = nstart;
            }

            if((i-start)>ans){
                ans = i-start;
            }
            vmap[s[i]] = i;
        }
        return ans;

    }
};

# 滑动窗口
class Solution2 {
public:
    int lengthOfLongestSubstring(string s) {
        int len = s.length();
        int ans = 0;
        int start = 0;
        for(int i=0; i<len; i++){
            for(int j=start; j<i; j++){
                if(s[i]==s[j]){
                    start=j+1;
                    break;
                }
            }
            if(i-start+1>ans){
                ans = i-start+1;
            }
        }
        return ans;

    }
};