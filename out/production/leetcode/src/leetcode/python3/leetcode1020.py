#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
    飞地数量
"""
from typing import List

# stack思路 688ms
class Solution:
    def numEnclaves(self, A: List[List[int]]) -> int:
        if len(A) < 3 or len(A[0]) < 3:
            return 0
        num = sum([sum(x) for x in A])
        row_num, column = len(A), len(A[0])
        path_set = set()

        for i in range(column):
            if A[0][i]:
                path_set.add((0, i))
                num -= 1
            if A[row_num - 1][i]:
                path_set.add((row_num - 1, i))
                num -= 1

        for i in range(1, row_num - 1):
            if A[i][0]:
                path_set.add((i, 0))
                num -= 1
            if A[i][column - 1]:
                path_set.add((i, column - 1))
                num -= 1
        path_queue = list(path_set)

        while len(path_queue):
            q = path_queue.pop()
            if q[0] > 0 and (q[0] - 1, q[1]) not in path_set and A[q[0] - 1][q[1]]:
                path_set.add((q[0] - 1, q[1]))
                path_queue.append((q[0] - 1, q[1]))
                num -= 1

            if q[1] > 0 and (q[0], q[1] - 1) not in path_set and A[q[0]][q[1] - 1]:
                path_set.add((q[0], q[1] - 1))
                path_queue.append((q[0], q[1] - 1))
                num -= 1

            if q[0] < row_num - 1 and (q[0] + 1, q[1]) not in path_set and A[q[0] + 1][q[1]]:
                path_set.add((q[0] + 1, q[1]))
                path_queue.append((q[0] + 1, q[1]))
                num -= 1

            if q[1] < column - 1 and (q[0], q[1] + 1) not in path_set and A[q[0]][q[1] + 1]:
                path_set.add((q[0], q[1] + 1))
                path_queue.append((q[0], q[1] + 1))
                num -= 1

        return num

# 递归思路 708ms
class Solution2:
    def numEnclaves(self, A: List[List[int]]) -> int:
        if len(A) < 3 or len(A[0]) < 3:
            return 0
        row_num, column_num = len(A), len(A[0])

        def dfs(i, j):
            if i < 0 or i >= row_num: return
            if j < 0 or j >= column_num: return
            if A[i][j]:
                A[i][j] = 0
                dfs(i - 1, j)
                dfs(i + 1, j)
                dfs(i, j - 1)
                dfs(i, j + 1)

        for i in range(column_num):
            dfs(0, i)
            dfs(row_num - 1, i)
        for i in range(row_num):
            dfs(i, 0)
            dfs(i, column_num - 1)

        return sum([sum(x) for x in A])