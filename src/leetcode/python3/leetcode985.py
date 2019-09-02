#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    查询后的偶数和
"""
from typing import List


# 按照规则
class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        sum_a = sum([a for a in A if a % 2 == 0])
        res = []
        for val, ind in queries:
            if (A[ind] + val) % 2 == 0:
                if A[ind] % 2 == 0:
                    sum_a += val
                else:
                    sum_a += val + A[ind]
            else:
                if A[ind] % 2 == 0:
                    sum_a -= A[ind]

            res.append(sum_a)
            A[ind] += val

        return res