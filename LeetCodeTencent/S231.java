package LeetCodeTencent;

/**
 * @author Yang Lei
 * @date 2021/1/15
 */
public class S231 {
    public boolean isPowerOfTwo(int n) {
        int i = n & n - 1 ;
        return (i == 0) && n > 0;
    }

    public static void main(String[] args) {
        S231 s231 = new S231();
        boolean powerOfTwo = s231.isPowerOfTwo(8);
        System.out.println(powerOfTwo);
    }
}
