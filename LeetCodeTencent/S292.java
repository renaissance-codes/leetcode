package LeetCodeTencent;

/**
 * @author Yang Lei
 * @date 2021/1/19
 */
public class S292 {
    public static void main(String[] args) {
        S292 s292 = new S292();
        System.out.println(s292.canWinNim(10));
    }

    public boolean canWinNim(int n) {
        return (n % 4 != 0);
    }
}
