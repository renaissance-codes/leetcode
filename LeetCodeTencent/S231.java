package LeetCodeTencent;

/**
 * @author Yang Lei
 * @date 2021/1/15
 */
public class S231 {
    public boolean isPowerOfTwo(int n) {
        int l = 1;
        int m = 0;
        while(l <= 32){
            m = m << l;
            int d  = n ^ m;
            if(d==0){
                return true;
            }
            l = l +1;
        }
        return false;
    }
}
