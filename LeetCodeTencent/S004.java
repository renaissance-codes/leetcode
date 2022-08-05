package LeetCodeTencent;

import java.util.Arrays;

/**
 * @author Yang Lei
 * @date 2021/1/11
 */
public class S004 {
    public static void main(String[] args) {
        S004 s004 = new S004();
        int a[] = {1, 2};
        int b[] = {2, 3, 5, 6};

        double v = s004.FindMedianSortedArrays(a, b);
        double v2 = s004.FindMedianSortedArrays2(a, b);
        System.out.println(v);
        System.out.println(v2);
    }

    public double FindMedianSortedArrays2(int[] nums1, int[] nums2) {
        // 合并两个数组，并排序（取巧的方法，不推荐）
        int len1 = nums1.length;
        int len2 = nums2.length;
        int len = len1 + len2;
        int[] nums = new int[len];

        nums = Arrays.copyOf(nums1, len);
        System.arraycopy(nums2, 0, nums, len1, len2);
        Arrays.sort(nums);
        if (len % 2 == 0) {
            return (nums[len / 2] + nums[len / 2 - 1]) * 0.5;
        }
        return nums[len / 2];
    }

    public double FindMedianSortedArrays(int[] nums1, int[] nums2) {

        // 构造大小(m + n + 1) / 2的数组，统计边界情况
        int m = nums1.length;
        int n = nums2.length;
        if (m > n) {
            return FindMedianSortedArrays(nums2, nums1);
        }
        //数组大小的一半
        int k = (m + n + 1) / 2;
        int left = 0;
        int right = m;
        //循环遍历，二分法
        while (left < right) {
            int i = (left + right) / 2;
            int j = k - i;
            if (nums1[i] < nums2[j - 1]) {
                left = i + 1;
            } else {
                right = i;
            }
        }
        int m1 = left;
        int m2 = k - left;
        int c1 = Math.max(m1 == 0 ? Integer.MIN_VALUE : nums1[m1 - 1],
                m2 == 0 ? Integer.MIN_VALUE : nums2[m2 - 1]);

        if ((m + n) % 2 == 1) {
            return c1;
        }

        int c2 = Math.min(m1 == m ? Integer.MAX_VALUE : nums1[m1],
                m2 == n ? Integer.MAX_VALUE : nums2[m2]);
        return (c1 + c2) * 0.5;
    }
}
