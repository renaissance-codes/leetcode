#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    叶值的最小代价生成树
"""
from typing import List


# 使用自底向上，加上存储的动态规划方法
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        if len(arr) == 2:
            return arr[0] * arr[1]
        dlen = len(arr)
        cache = [[-1 for i in range(dlen)] for j in range(dlen)]

        def mcSub(i, j):
            if i == j:
                cache[i][j] = 0
                return 0
            elif j - i == 1:
                v = arr[i] * arr[j]
                cache[i][j] = v
                return v
            else:
                minv = 1 << 32
                for x in range(i, j):
                    left = -1
                    if cache[i][x] != -1:
                        left = cache[i][x]
                    else:
                        left = mcSub(i, x)
                    lefti = max(arr[i:x + 1])

                    right = -1
                    if cache[x + 1][j] != -1:
                        right = cache[x + 1][j]
                    else:
                        right = mcSub(x + 1, j)
                    righti = max(arr[x + 1:j + 1])
                    val = lefti * righti + left + right

                    if minv > val:
                        minv = val
                cache[i][j] = minv
                return minv

        return mcSub(0, dlen - 1)


# 增加了求最大值预存储  144ms
class Solution2:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        if len(arr) == 2:
            return arr[0] * arr[1]
        dlen = len(arr)
        cache = [[-1 for i in range(dlen)] for j in range(dlen)]
        maxarr = [[arr[i] if i == j else 0 for i in range(dlen)] for j in range(dlen)]
        for i in range(1, dlen):
            for j in range(dlen - i):
                maxarr[j][j + i] = max(maxarr[j][j], maxarr[j + 1][j + i])

        def mcSub(i, j):
            if i == j:
                cache[i][j] = 0
                return 0
            elif j - i == 1:
                v = arr[i] * arr[j]
                cache[i][j] = v
                return v
            else:
                minv = 1 << 32
                for x in range(i, j):
                    left = -1
                    if cache[i][x] != -1:
                        left = cache[i][x]
                    else:
                        left = mcSub(i, x)
                    lefti = maxarr[i][x]

                    right = -1
                    if cache[x + 1][j] != -1:
                        right = cache[x + 1][j]
                    else:
                        right = mcSub(x + 1, j)
                    righti = maxarr[x + 1][j]

                    val = lefti * righti + left + right

                    if minv > val:
                        minv = val
                cache[i][j] = minv
                return minv

        return mcSub(0, dlen - 1)


# 贪心算法28ms
class Solution3:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        stack = [1<<32]
        ans = 0
        for n in arr:
            while stack[-1] < n:
                ans +=  stack.pop() * min(stack[-1], n)
            stack.append(n)
        while len(stack) > 2:
            ans +=  stack.pop() * stack[-1]
        return ans
