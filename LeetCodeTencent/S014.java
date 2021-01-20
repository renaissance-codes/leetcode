package LeetCodeTencent;

/**
 * @author Yang Lei
 * @date 2021/1/20
 */
public class S014 {

    public static void main(String[] args) {
        S014 s014 = new S014();
        String[] strings = new String[]{};
        System.out.println(s014.longestCommonPrefix(strings));
    }

    public String longestCommonPrefix(String[] strs) {
        if (strs.length == 0) {
            return "";
        }
        if (strs.length == 1) {
            return strs[0];
        }
        String res = strs[0];
        for (int i = 1; i < strs.length; i++) {
            res = getPrefix(res, strs[i]);
        }
        return res;
    }

    private String getPrefix(String res, String str) {
        int resLen = res.length();
        int strLen = str.length();
        int min = Math.min(resLen, strLen);
        String prefix = "";
        for (int i = 0; i < min; i++) {
            if (res.charAt(i) == str.charAt(i)) {
                prefix = res.substring(0, i + 1);
            } else {
                return prefix;
            }
        }
        return prefix;

    }
}
