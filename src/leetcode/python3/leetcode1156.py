#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    单字符重复子串的最大长度
"""


class Solution:
    """
        对每个字母进行分别统计重复子串的情况
    """
    def maxRepOpt1(self, text: str) -> int:
        d = {}
        last = "@"
        start_indx = -1
        for i, x in enumerate(text):
            if x == last:
                continue
            else:
                if last != "@":
                    d[last].append((start_indx, i - 1))
                d.setdefault(x, [])

                last = x
                start_indx = i
        d[last].append((start_indx, len(text) - 1))

        max_v = -1

        for k, v in d.items():
            if len(v) == 1:
                s, e = v[0]
                max_v = max(max_v, e - s + 1)
            else:
                st, et = v[0]
                max_v = max(max_v, et - st + 2)
                for s, e in v[1:]:
                    if s - et > 2:
                        max_v = max(max_v, e - s + 2)
                    else:
                        if len(v) > 2:
                            max_v = max(max_v, e - st + 1)
                        else:
                            max_v = max(max_v, e - st)
                    st, et = s, e
        return max_v
