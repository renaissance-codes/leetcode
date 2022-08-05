#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    索引处的解码字符串
"""

# 思路：存储分段字符串 48ms
class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:
        indx = 0
        result_s = ""
        tempt_list = []
        tempt_s = ""
        store_s = []
        repeat = 0
        for s in S:
            if s.isalpha():
                if not tempt_list and tempt_s:
                    store_s.append((tempt_s, repeat))
                indx += 1
                tempt_list.append(s)
                if indx == K:
                    result_s = s
                    break
            else:
                if tempt_list:
                    tempt_s = "".join(tempt_list)
                    repeat = int(s)
                    tempt_list = []
                else:
                    repeat *= int(s)
                indx *= int(s)

                if indx >= K:
                    if store_s:
                        s_list = []

                        s_len = 0
                        rp = 1
                        for ss, sp in store_s:
                            slen = len(ss) + rp * s_len
                            s_list.append(slen)
                            rp = sp
                            s_len = slen
                        ts_len = len(tempt_s)
                        k = K - 1
                        ts_str = tempt_s
                        for i, st in enumerate(s_list[::-1]):
                            rp = store_s[-(i + 1)][1]
                            st_len = st * rp + ts_len

                            k = k % st_len

                            if k >= st * rp:
                                result_s = ts_str[k - st * rp]
                                break
                            else:

                                ts_str = store_s[-(i + 1)][0]
                                ts_len = len(ts_str)

                                if i + 1 == len(store_s):
                                    k = k % ts_len
                                    result_s = ts_str[k]

                        # k = k%ts_len
                        # result_s = ts_str[k]
                    else:
                        k = (K - 1) % len(tempt_s)
                        result_s = tempt_s[k]
                    break

        return result_s


# 先加密然后解码
class Solution2:
    def decodeAtIndex(self, S: str, K: int) -> str:
        size = 0

        for s in S:
            if s.isalpha():
                size += 1
            else:
                size *= int(s)

        for s in S[::-1]:
            K %= size

            if K == 0 and s.isalpha():
                return s

            if s.isalpha():
                size -= 1
            else:
                size //= int(s)
        return ""
