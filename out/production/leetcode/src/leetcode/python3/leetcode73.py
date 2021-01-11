#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    矩阵置零
"""
from typing import List


# 原地算法
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        if row == 0:
            return
        column = len(matrix[0])

        for i in range(row):
            for j in range(column):
                matrix[i][j] <<= 1
                matrix[i][j] += 1

        for i in range(row):
            for j in range(column):
                if (matrix[i][j] >> 1) == 0:
                    matrix[i][j] = 2

                    for k in range(row):
                        if k != i:
                            matrix[k][j] = matrix[k][j] >> 1 << 1

                    for k in range(column):
                        if k != j:
                            matrix[i][k] = matrix[i][k] >> 1 << 1

        for i in range(row):
            for j in range(column):
                if matrix[i][j] & 1:
                    matrix[i][j] >>= 1
                else:
                    matrix[i][j] = 0


# 更为有效的策略，使用O(1)空间复杂度，和更少的时间复杂度
# 使用边缘位置存储状态
class Solution2:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        if row == 0:
            return
        column = len(matrix[0])

        iscolum = False
        for i in range(row):
            if matrix[i][0] == 0:
                iscolum = True

            for j in range(1, column):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, row):
            for j in range(1, column):
                if not matrix[i][0] or not matrix[0][j]:
                    matrix[i][j] = 0

        if matrix[0][0] == 0:
            for j in range(1, column):
                matrix[0][j] = 0
        if iscolum:
            for i in range(row):
                matrix[i][0] = 0
