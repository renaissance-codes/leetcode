#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
    查询矩阵数据
"""

# 思路类似于二分法，比较矩阵中间的数，留下三个部分继续比较， 68ms
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row = len(matrix)
        if row == 0:
            return False

        column = len(matrix[0])
        if column == 0:
            return False

        if matrix[0][0] > target:
            return False

        if matrix[-1][-1] < target:
            return False

        return self.searchSmall(0, row, 0, column, matrix, target)

    def searchSmall(self, row_top, row_bottom, column_left, column_right, maxtrix, target):

        if row_top > row_bottom or column_left > column_right:
            return False

        if row_top == row_bottom and row_top == len(maxtrix):
            return False

        if column_left == column_right and column_left == len(maxtrix[0]):
            return False
        if row_top == row_bottom and column_left == column_right:
            return maxtrix[row_top][column_left] == target

        row_half = (row_top + row_bottom) // 2
        colum_half = (column_left + column_right) // 2

        if maxtrix[row_half][colum_half] == target:
            return True

        if maxtrix[row_half][colum_half] > target:
            return self.searchSmall(row_top, row_half - 1, column_left, colum_half - 1, maxtrix,
                                    target) or self.searchSmall(row_half, row_bottom, column_left, colum_half - 1,
                                                                maxtrix, target) or self.searchSmall(row_top,
                                                                                                     row_half - 1,
                                                                                                     colum_half,
                                                                                                     column_right,
                                                                                                     maxtrix, target)
        else:
            return self.searchSmall(row_half + 1, row_bottom, column_left, colum_half, maxtrix,
                                    target) or self.searchSmall(row_top, row_half, colum_half + 1, column_right,
                                                                maxtrix, target) or self.searchSmall(row_half + 1,
                                                                                                     row_bottom,
                                                                                                     colum_half + 1,
                                                                                                     column_right,
                                                                                                     maxtrix, target)