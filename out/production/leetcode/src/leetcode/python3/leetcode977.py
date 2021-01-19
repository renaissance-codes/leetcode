#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
    有序数组的平方
"""
from typing import List

# 最直接的思路, 340ms
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        A.sort(key=lambda x: abs(x))
        return [x**2 for x in A]


# 双指针
class Solution2:
    def sortedSquares(self, A: List[int]) -> List[int]:
        if len(A) < 2:
            return [x ** 2 for x in A]
        negative_index = len(A) - 1
        for i, e in enumerate(A):
            if e > 0:
                negative_index = i - 1
                break
        if negative_index < 0:
            return [x ** 2 for x in A]
        if negative_index == len(A) - 1:
            return [x ** 2 for x in A[::-1]]

        positive_index = negative_index + 1

        result = []
        while positive_index < len(A) and negative_index >= 0:
            if A[positive_index] < -A[negative_index]:
                result.append(A[positive_index] ** 2)
                positive_index += 1
            else:
                result.append(A[negative_index] ** 2)
                negative_index -= 1

        if positive_index < len(A):
            return result + [x ** 2 for x in A[positive_index:]]
        if negative_index >= 0:
            return result + [A[i] ** 2 for i in range(negative_index, -1, -1)]