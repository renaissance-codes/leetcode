class Solution {
public:
    string convert(string s, int numRows) {
        string res = "";
        int slen = s.size();
        if(numRows<2){
            return s;
        }
        for(int i=0; i<numRows; i++){
            if(i==0){
                int j = 0;
                while(j<slen){
                    res += s[j];
                    j += 2*numRows-2;
                }
            }else if(i==numRows-1){
                int j = numRows-1;
                while(j<slen){
                    res += s[j];
                    j += 2*numRows-2;
                }
            }else{
                int j = i;
                int sign = 1;
                while(j<slen){
                    res += s[j];
                    if(sign>0){
                        j += 2*numRows-2-2*i;
                    }else{
                        j += 2*i;
                    }
                    sign *= -1;
                }
            }
        }
        return res;
    }
};