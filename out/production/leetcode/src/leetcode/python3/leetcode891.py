#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    子序列宽度之和
"""
from typing import List
from copy import deepcopy

# 超时
class Solution:
    def sumSubseqWidths(self, A: List[int]) -> int:
        d_dict = {}
        d_len = len(A)
        ans = 0
        for j in range(d_len):
            n_dict = deepcopy(d_dict)
            jvalue= A[j]
            for k, v in d_dict.items():
                if k[0] > jvalue:
                    n_dict.setdefault((jvalue, k[1]), 0)
                    n_dict[(jvalue, k[1])] += v
                    ans += (k[1]-jvalue)*v
                elif k[1] < jvalue:
                    n_dict.setdefault((k[0], jvalue), 0)
                    n_dict[(k[0], jvalue)] += v
                    ans += (jvalue-k[0])*v
                else:
                    n_dict[(k[0], k[1])] += v
                    ans += (k[1]-k[0])*v
            n_dict.setdefault((jvalue, jvalue), 0)
            n_dict[(jvalue, jvalue)] += 1
            d_dict = n_dict
        return ans % (10**9+7)


# 利用推导公式
class Solution2:
    def sumSubseqWidths(self, A: List[int]) -> int:
        ans = 0
        A.sort()
        d_len = len(A)
        h_len = (d_len+1)>>1
        for i in range(h_len):
            ans += (A[d_len-i-1]-A[i])*((1<<(d_len-i-1))-(1<<i))
        return ans % (10**9+7)

