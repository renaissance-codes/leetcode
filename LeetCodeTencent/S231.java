package LeetCodeTencent;

/**
 * @author Yang Lei
 * @date 2021/1/15
 */
public class S231 {
    public boolean isPowerOfTwo(int n) {
        while (n > 0) {
            n = n >> 1;
            if(n ==1){
                return true;
            }
        }
        return false;
    }
}
