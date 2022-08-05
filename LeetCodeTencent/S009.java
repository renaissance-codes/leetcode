package LeetCodeTencent;

/**
 * @author Yang Lei
 * @date 2021/1/20
 */
public class S009 {
    public static void main(String[] args) {
        S009 s009 = new S009();
        System.out.println(s009.isPalindrome(1000030001));
    }

    public boolean isPalindrome(int x) {
        if (x < 0) {
            return false;
        }
        if (x >= 0 && x < 10) {
            return true;
        }
        String s = String.valueOf(x);
        int length = s.length();
        for (int i = 0; i < length; i++) {
            String s1 = String.valueOf(s.charAt(0));

            if (!s.endsWith(s1)) {
                return false;
            } else {
                if (s.length() <= 2) {
                    return true;
                }
            }
            s = s.substring(1, s.length() - 1);
        }
        return true;
    }


}
