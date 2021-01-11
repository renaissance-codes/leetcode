#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    正则表达式匹配
"""


# 动态规则的方法，自底向上
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if len(s) == 0 and len(p) == 0:
            return True

        pa = []
        last = ""
        for sp in p:
            if sp == "*":
                x = pa.pop()
                pa.append(x + sp)
            else:
                pa.append(sp)
        if len(s) == 0:
            return all([len(x) == 2 for x in pa])

        dp = [[0 for i in range(len(s) + 1)] for j in range(len(pa) + 1)]
        dp[0][0] = 1
        for i, x in enumerate(pa):
            for j, y in enumerate(s):
                if len(x) == 2:
                    if y == x[0] or x[0] == ".":
                        dp[i + 1][j + 1] = max([dp[i][j], dp[i][j + 1], dp[i + 1][j]])
                    else:
                        dp[i + 1][j + 1] = max(dp[i][j + 1], 0)
                    dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
                else:
                    if y == x[0] or x[0] == ".":
                        dp[i + 1][j + 1] = dp[i][j]
                    else:
                        dp[i + 1][j + 1] = 0

        return dp[len(pa)][len(s)]

