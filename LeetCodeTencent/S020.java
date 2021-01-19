package LeetCodeTencent;

import java.util.ArrayList;
import java.util.Stack;

/**
 * @author Yang Lei
 * @date 2021/1/19
 */
public class S020 {
    public static void main(String[] args) {
        S020 s020 = new S020();
        System.out.println(s020.isValid("(("));
    }

    public boolean isValid(String s) {
        if (s.length() < 2) {
            return false;
        }
        ArrayList<Character> chars = new ArrayList<>();
        chars.add('[');
        chars.add('{');
        chars.add('(');

        Stack<Character> strings = new Stack<>();
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (chars.contains(c)) {
                strings.add(c);
            } else {
                if (strings.isEmpty()) {
                    return false;
                }
                Character pop = strings.pop();
                Character pairChar = getPairChar(pop);
                if (c != pairChar) {
                    return false;
                }
            }
        }
        if(strings.isEmpty()){
            return true;
        }
        return false;
    }

    private Character getPairChar(char c) {
        if (c == '{') {
            return '}';
        } else if (c == '(') {
            return ')';
        } else if (c == '[') {
            return ']';
        }
        return ' ';
    }
}
