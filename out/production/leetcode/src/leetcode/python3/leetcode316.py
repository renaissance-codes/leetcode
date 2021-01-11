#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    去除重复字符串
"""

# 156ms
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:

        rn = 0
        s_len = len(s)
        ans = ""
        s_set = set()
        start = 0
        end = s_len - 1
        ds = len(set(s))
        while rn < ds:

            tset = set()

            j = s_len
            while len(tset) < ds - rn:
                j -= 1
                if s[j] in s_set:
                    continue
                tset.add(s[j])

            c = "~"
            min_i = -1
            for i in range(start, min(j + 1, s_len)):
                if s[i] in s_set:
                    continue
                if s[i] < c:
                    c = s[i]
                    min_i = i
            start = min_i + 1
            s_set.add(c)
            ans += c
            rn += 1
        return ans


# 使用栈思路
class Solution2:
    def removeDuplicateLetters(self, s: str) -> str:

        max_ind = {x: i for i, x in enumerate(s)}

        ans = ""
        for i, x in enumerate(s):
            if x in ans:
                continue
            while ans[-1:] > x and max_ind[ans[-1:]] > i:
                ans = ans[:-1]
            ans += x
        return ans
