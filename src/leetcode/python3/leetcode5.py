#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
    寻找最长回文字符串
"""


# 比较朴素的思路，使用额外空间存储短字符串是否是回文字符串，时间5968ms, 效率不够高
class Solution:

    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        s_metric = [[1 if i == j else 0 for j in range(len(s))] for i in range(len(s))]
        longest_s = s[0]
        longest_len = 1
        while len(s) - longest_len:
            for i in range(len(s) - longest_len):
                if longest_len == 1:
                    if s[i] == s[i + longest_len]:
                        s_metric[i][i + longest_len] = 1
                        longest_s = s[i:i + longest_len + 1]
                else:
                    if s_metric[i + 1][i + longest_len - 1] and s[i] == s[i + longest_len]:
                        s_metric[i][i + longest_len] = 1
                        longest_s = s[i:i + longest_len + 1]
            longest_len += 1

        return longest_s
