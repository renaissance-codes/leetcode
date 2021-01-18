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
        int step = 0;
        for (int i = 0; i < n; i++) {
            start = i + start;
            step = start + step;
        }
        return start + step;
    }

    public static void main(String[] args) {
        S070 s070 = new S070();
        System.out.println(s070.climbStairs(1));

    }
}
