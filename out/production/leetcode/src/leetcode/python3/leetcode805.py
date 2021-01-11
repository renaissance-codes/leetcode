#!/usr/bin/env python
# -*- coding:utf-8 -*-


"""
    均值分割，将数组分为两个均值相等的数组
"""
from typing import List


# 暴力解法
class Solution:
    def splitArraySameAverage(self, A: List[int]) -> bool:
        a_len = len(A)
        if a_len < 2:
            return False
        if a_len == 2:
            return A[0] == A[1]
        sum_a = sum(A)
        m = a_len // 2
        possible = False
        for i in range(1, m + 1):
            if sum_a * i % a_len == 0:
                possible = True
                break
        if not possible:
            return False

        A.sort()

        dps = [set() for _ in range(a_len + 1)]
        dps[0].add(0)

        for j in range(a_len):
            for i in range(m, 0, -1):
                for x in dps[i - 1]:
                    dps[i].add(x + A[j])

        for i in range(1, m + 1):
            if sum_a * i % a_len == 0 and sum_a * i // a_len in dps[i]:
                return True
        return False

#
class Solution2:
    def splitArraySameAverage(self, A: List[int]) -> bool:
        a_len = len(A)
        if a_len < 2:
            return False
        if a_len == 2:
            return A[0] == A[1]
        sum_a = sum(A)
        m = a_len // 2
        A.sort()
        for i in range(1, m + 1):
            if sum_a * i % a_len == 0 and self.dfs(A, 0, i, sum_a * i / a_len):
                return True

        return False

    def dfs(self, A: List[int], begin: int, num: int, target: float) -> bool:
        if num == 0:
            return target == 0

        if A[begin] * num > target:
            return False

        for i in range(begin, len(A) - num + 1):
            if i > begin and A[i] == A[i - 1]:
                continue
            d = self.dfs(A, i + 1, num - 1, target - A[i])
            if d:
                return True
        return False