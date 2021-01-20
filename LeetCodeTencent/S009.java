package LeetCodeTencent;

/**
 * @author Yang Lei
 * @date 2021/1/20
 */
public class S009 {
    public boolean isPalindrome(int x) {
        if (x < 11) {
            return false;
        }
        String s = String.valueOf(x);
        for (int i = 0; i < s.length(); i++) {
            String s1 = String.valueOf(s.charAt(i));

            if (!s.endsWith(s1)) {
                return false;
            }else{
                if(s.length()==2){
                    return true;
                }
            }
            s = s.substring(i + 1, s.length() - 1);
        }
        return true;
    }

    public static void main(String[] args) {
        S009 s009 = new S009();
        System.out.println(s009.isPalindrome(2112));
    }


}
