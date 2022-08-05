#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    有序队列
"""


# 分两种情况处理 80ms
class Solution:
    def orderlyQueue(self, S: str, K: int) -> str:
        if K == 1:
            st = "~"
            sd = {}
            for i, s in enumerate(S):
                sd.setdefault(s, [])
                sd[s].append(i)
                if s < st:
                    st = s
            candicate_list = sorted([S[i:] + S[:i] for i in sd[st]])

            return candicate_list[0]

        else:
            s_list = sorted([s for s in S])
            return "".join(s_list)


# 48ms
class Solution2:
    def orderlyQueue(self, S: str, K: int) -> str:
        if K == 1:
            s_right = ""
            s_start = S
            min_s = min(list(S))
            ans = "~"
            while True:
                n_i = s_start.find(min_s)
                if n_i < 0:
                    break
                else:
                    ns = s_start[n_i:] + s_right + s_start[:n_i]
                    if ns < ans:
                        ans = ns
                    s_right += s_start[:n_i + 1]
                    s_start = s_start[n_i + 1:]
            return ans

        else:
            s_list = sorted(list(S))
            return "".join(s_list)