#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
    将矩阵中的所有相邻的数字进行变换
"""
from typing import List

# 暴力破解, 188ms
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        row_num = len(image)
        column_num = len(image[0])
        que = [(sr, sc)]
        color = image[sr][sc]
        s_set = {(sr, sc)}
        while len(que):
            q = que.pop(0)
            image[q[0]][q[1]] = newColor
            if q[0] > 0 and (q[0] - 1, q[1]) not in s_set and image[q[0] - 1][q[1]] == color:
                que.append((q[0] - 1, q[1]))
                s_set.add((q[0] - 1, q[1]))
            if q[1] > 0 and (q[0], q[1] - 1) not in s_set and image[q[0]][q[1] - 1] == color:
                que.append((q[0], q[1] - 1))
                s_set.add((q[0], q[1] - 1))
            if q[0] < row_num - 1 and (q[0] + 1, q[1]) not in s_set and image[q[0] + 1][q[1]] == color:
                que.append((q[0] + 1, q[1]))
                s_set.add((q[0] + 1, q[1]))
            if q[1] < column_num - 1 and (q[0], q[1] + 1) not in s_set and image[q[0]][q[1] + 1] == color:
                que.append((q[0], q[1] + 1))
                s_set.add((q[0], q[1] + 1))
        return image

# 略微改进 116ms
class Solution2:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        row_num = len(image)
        column_num = len(image[0])
        que = [(sr, sc)]
        color = image[sr][sc]
        s_metric = [[1 for _ in range(column_num)] for j in range(row_num)]
        s_metric[sr][sc] = 0
        while len(que):
            p, q = que.pop(0)
            image[p][q] = newColor
            if p > 0 and s_metric[p-1][q] and image[p-1][q] == color:
                que.append((p-1, q))
                s_metric[p-1][q] = 0
            if q > 0 and s_metric[p][q-1] and image[p][q-1] == color:
                que.append((p, q-1))
                s_metric[p][q-1] = 0
            if p < row_num-1 and s_metric[p+1][q] and image[p+1][q] == color:
                que.append((p+1, q))
                s_metric[p+1][q] = 0
            if q < column_num-1 and s_metric[p][q+1] and image[p][q+1] == color:
                que.append((p, q+1))
                s_metric[p][q+1] = 0
        return image

# 100ms
class Solution3:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        row_num, column_num = len(image), len(image[0])

        color = image[sr][sc]
        if color == newColor:
            return image

        que = [(sr, sc)]

        while que:
            p, q = que.pop()

            if p < 0 or p >= row_num or q < 0 or q >= column_num:
                continue

            if image[p][q] != color:
                continue

            image[p][q] = newColor

            for i, j in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                que.append((p + i, q + j))
        return image
