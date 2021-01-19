package LeetCodeTencent;

import java.util.HashSet;

/**
 * @author Yang Lei
 * @date 2021/1/19
 */
public class S217 {
    public static void main(String[] args) {
        S217 s217 = new S217();
        s217.containsDuplicate(new int[]{1, 2, 3});
    }

    public boolean containsDuplicate(int[] nums) {
        HashSet<Integer> ints = new HashSet<Integer>();
        for (int num : nums) {
            if (ints.contains(num)) {
                return true;
            } else {
                ints.add(num);
            }
        }
        return false;
    }
}
