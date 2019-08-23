#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    和被K整除的的子数组
"""

from collections import Counter
from typing import List


# 动态规划 还是超时了
class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        num = 0
        d_len = len(A)
        sum_list = [0]
        sum_s = 0
        for x in A:
            sum_s += x
            sum_list.append(sum_s % K)

        last_v = []
        left = 0
        left_dict = {}
        last_dict = {}
        for i, x in enumerate(A):
            if x % K == 0:
                num += left + 1
                left += 1
            else:
                k = 0
                lft = 0
                for j in last_v:
                    sum_s = sum_list[i + 1] - sum_list[j]
                    if sum_s % K == 0:
                        lft = left_dict[j] + 1
                        num += lft
                        break

                    k += 1
                if lft:
                    last_v.pop(k)
                last_v.insert(0, i)

                left_dict[i] = left
                left = lft
                # last_v = nlast + last_v[k+1:]

        return num


# 巧妙地思路, 利用前缀数组来做 444ms
class Solution2:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        sum_list = [0]
        sum_s = 0
        for x in A:
            sum_s += x
            sum_list.append(sum_s % K)
        count = Counter(sum_list)

        return sum([x * (x - 1) // 2 for x in count.values()])