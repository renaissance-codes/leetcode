#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    不邻接植花
"""
from typing import List


# 存储路径 1056ms
class Solution:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        if len(paths) == 0:
            return [1] * N

        x_set = set()
        path_dict = {}
        for x, y in paths:
            if x > y:
                path_dict.setdefault(x - 1, set())
                path_dict[x - 1].add(y - 1)
            else:
                path_dict.setdefault(y - 1, set())
                path_dict[y - 1].add(x - 1)
        result = []
        for x in range(N):
            if x not in path_dict:
                result.append(1)
                continue
            x_set = {result[j] for j in path_dict[x]}
            for j in range(1, N + 1):
                if j not in x_set:
                    result.append(j)
                    break

        return result

# 632ms
class Solution2:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        if len(paths) == 0:
            return [1] * N

        x_set = set()
        path_dict = {}
        for x, y in paths:
            if x > y:
                path_dict.setdefault(x - 1, set())
                path_dict[x - 1].add(y - 1)
            else:
                path_dict.setdefault(y - 1, set())
                path_dict[y - 1].add(x - 1)
        result = [1 for _ in range(N)]
        item_list = list(path_dict.keys())
        item_list.sort()
        for xj in item_list:
            x_set = {result[j] for j in path_dict[xj]}
            for j in range(1, N + 1):
                if j not in x_set:
                    result[xj] = j
                    break

        return result


# 596ms
class Solution3:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:

        path_dict = {}
        for x, y in paths:
            if x > y:
                path_dict.setdefault(x - 1, [])
                path_dict[x - 1].append(y - 1)
            else:
                path_dict.setdefault(y - 1, [])
                path_dict[y - 1].append(x - 1)

        result = [1 for _ in range(N)]
        for xj in range(N):
            if xj not in path_dict:
                continue
            result[xj] = ({1, 2, 3, 4} - {result[j] for j in path_dict[xj]}).pop()

        return result
