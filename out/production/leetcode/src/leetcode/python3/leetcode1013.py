#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
    划分数组为三个部分
"""
from typing import List


# 简单思路，从两边向中间靠近， 464ms
class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        v = sum(A)
        if v % 3:
            return False

        v //= 3

        a_len = len(A)

        left = A[0]
        right = A[-1]
        i = 0
        j = a_len - 1

        while i < j:
            if left == v and right == v:
                return True
            if left != v:
                i += 1
                left += A[i]
            if right != v:
                j -= 1
                right += A[j]
        return False


# 计算累积三等分值的次数
class Solution2:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        v = sum(A)
        if v % 3:
            return False

        v //= 3
        a_len = len(A)
        temp = 0
        f1 = 0
        for x in A[:a_len - 1]:
            temp += x
            if temp == v:
                temp = 0
                f1 += 1
                if f1 == 2:
                    return True
        return False