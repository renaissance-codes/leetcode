#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    最短回文串
"""


# 用manacher 算法
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return s
        vs = "#" + "#".join(list(s)) + "#"
        slen = len(s) * 2 + 1
        mx = 0
        hf = 0
        mp = [0 for i in range(slen)]
        res = -1
        for i in range((slen >> 1) + 1):
            mp[i] = min(mx - i, mp[2 * hf - i]) if mx > i else 1
            while i - mp[i] >= 0 and i + mp[i] < slen and vs[i - mp[i]] == vs[i + mp[i]]:
                mp[i] += 1

            if i + mp[i] > mx:
                mx = i + mp[i]
                hf = i
            if i - mp[i] + 1 == 0 and mp[i] > res:
                res = mp[i]

        return s[res - 1:][::-1] + s

# 使用kmp算法
class Solution2:
    def shortestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return s
        ls = len(s)
        vs = s[::-1]
        nx = s + "*" + vs
        fx = [-1 for i in range(len(nx))]
        for i, x in enumerate(nx):
            if i == 0:
                fx[i] = 0
            else:
                t = fx[i - 1]
                while t > 0 and nx[t] != x:
                    t = fx[t - 1]
                if nx[t] == x:
                    t += 1
                fx[i] = t
        return vs[:len(s) - fx[-1]] + s
