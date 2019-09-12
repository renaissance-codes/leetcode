#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    分割数组的最大值， Split Array Largest Sum
"""
from typing import List


# 动态规划
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        num_sum = [0]
        for n in nums:
            num_sum.append(n + num_sum[-1])
        dlen = len(nums)
        ddict = {}

        def dfs(n, i):
            if n == 1:
                return num_sum[dlen] - num_sum[i]
            else:
                min_v = num_sum[dlen] - num_sum[i]
                for j in range(i + 1, dlen):
                    v1 = num_sum[j] - num_sum[i]
                    if v1 > min_v:
                        break
                    if (n - 1, j) in ddict:
                        v2 = ddict[(n - 1, j)]
                    else:
                        v2 = dfs(n - 1, j)
                        ddict[(n - 1, j)] = v2
                    min_v = min(min_v, max(v1, v2))
                return min_v

        return dfs(m, 0)


# 贪婪算法 + 二分法
class Solution2:
    def splitArray(self, nums: List[int], m: int) -> int:
        big = 0
        lit = 0
        for x in nums:
            big += x
            if x > lit:
                lit = x
        ans = big
        while big >= lit:
            mid = (big + lit) >> 1
            suma = 0
            cnt = 0
            for x in nums:
                if x + suma > mid:
                    cnt += 1
                    suma = x
                else:
                    suma += x
                if cnt > m:
                    break

            cnt += 1
            if cnt > m:
                lit = mid + 1
            else:
                ans = min(ans, mid)
                big = mid - 1
        return ans
