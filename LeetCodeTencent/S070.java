package LeetCodeTencent;

/**
 * @author Yang Lei
 * @date 2021/1/18
 */
public class S070 {
    public int climbStairs(int n) {
        if (n < 4) {
            return n;
        }
        int start = 0;
        int step = 1;
        int res = 1;
        for (int i = 0; i < n; i++) {
            res = start + step;
            start = step;
            step = res;
        }
        return res;
    }

    public static void main(String[] args) {
        S070 s070 = new S070();
        System.out.println(s070.climbStairs(5));

    }
}
