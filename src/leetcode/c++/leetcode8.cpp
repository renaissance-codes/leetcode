class Solution {
public:
    int myAtoi(string str) {
        int v = 0;
        int i = 0;
        int sign = 1;
        int slen = str.size();
        while(str[i]==' ') i++;
        if(i==slen) return 0;
        if(str[i]=='-'){
            sign = -1;
        }
        if(str[i]=='-' || str[i]=='+')
            i++;

        while(i<slen&&isdigit(str[i])){
            if(v>INT_MAX/10||(v==INT_MAX/10&&str[i]-48>7)){
                return sign>0?INT_MAX:INT_MIN;
            }
            v = v*10 + (str[i]-48);
            i++;
        }

        return sign>0?v:sign*v;

    }
};