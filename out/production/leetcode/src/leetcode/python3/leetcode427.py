#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
    四叉树的构建
"""
from typing import List

class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

# 180ms
class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        row_num, column = len(grid), len(grid)
        row_num_half, column_half = row_num // 2, column // 2

        sum_data = sum([sum(gd) for gd in grid])
        if sum_data == row_num * column:
            return Node(1, True, None, None, None, None)

        if sum_data == 0:
            return Node(0, True, None, None, None, None)

        topLeft = [gd[:column_half] for gd in grid[:row_num_half]]
        topRight = [gd[column_half:column] for gd in grid[:row_num_half]]
        bottomLeft = [gd[:column_half] for gd in grid[row_num_half:row_num]]
        bottomRight = [gd[column_half:column] for gd in grid[row_num_half:row_num]]

        topLeftNode = self.construct(topLeft)
        topRightNode = self.construct(topRight)
        bottomLeftNode = self.construct(bottomLeft)
        bottomRightNode = self.construct(bottomRight)

        return Node(1, False, topLeftNode, topRightNode, bottomLeftNode, bottomRightNode)
