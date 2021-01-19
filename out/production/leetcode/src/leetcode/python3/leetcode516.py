#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    最长回文子序列
"""


# 动态规划方法，超时
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        s_len = len(s)

        s_matrix = [[0] * (s_len + 1) for _ in range(s_len + 1)]

        max_v = 0
        for i in range(s_len - 1, -1, -1):
            for j in range(s_len):
                if s[i] == s[j]:
                    s_matrix[s_len - i][j + 1] = max(s_matrix[s_len - i - 1][j] + 1, s_matrix[s_len - i][j])
                else:
                    s_matrix[s_len - i][j + 1] = max(s_matrix[s_len - i][j], s_matrix[s_len - i - 1][j + 1])

        return s_matrix[s_len][s_len]

# 动态规划的另外思路
class Solution2:
    def longestPalindromeSubseq(self, s: str) -> int:
        s_len = len(s)

        s_matrix = [[0] * (s_len) for _ in range(s_len)]

        for i in range(s_len - 1, -1, -1):
            s_matrix[i][i] = 1
            for j in range(i + 1, s_len):
                if s[i] == s[j]:
                    s_matrix[i][j] = s_matrix[i + 1][j - 1] + 2

                else:
                    s_matrix[i][j] = max(s_matrix[i + 1][j], s_matrix[i][j - 1])
        return s_matrix[0][s_len - 1]


# 用一维数组来代替二位数组
class Solution3:
    def longestPalindromeSubseq(self, s: str) -> int:
        if s == s[::-1]:
            return len(s)

        s_len = len(s)

        dp = [0] * s_len

        for i in range(s_len):
            max_v = 0
            dp[i] = 1
            for j in range(i - 1, -1, -1):
                tmp = dp[j]
                if s[j] == s[i]:
                    dp[j] = max_v + 2
                max_v = max(tmp, max_v)

        for d in dp:
            max_v = max(d, max_v)

        return max_v
