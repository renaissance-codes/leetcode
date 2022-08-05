#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    优势洗牌
"""
from typing import List


# 使用启发式算法，田忌赛马的思路，如果相应索引的没有优势，那么就是用最小的对上最大的 668ms
class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        A.sort()
        b = [(x, i) for i,x in enumerate(B)]
        b.sort()
        a = []
        i = 0
        j = len(b)-1
        while A:
            x = A.pop(0)
            if x > b[i][0]:
                a.append((x, b[i][1]))
                i += 1
            else:
                a.append((x, b[j][1]))
                j -= 1
        a.sort(key=lambda x: x[1])
        return [x[0] for x in a]


class Solution2:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        A.sort()
        bsort = sorted([(x, i) for i, x in enumerate(B)])
        result = [0 for _ in A]
        i = 0
        j = len(B)-1
        for x in A:
            if x > bsort[i][0]:
                result[bsort[i][1]] = x
                i += 1
            else:
                result[bsort[j][1]] = x
                j -= 1
        return result


class Solution3:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        A.sort()
        bsort = sorted(range(len(B)), key=lambda x: B[x])
        B = [B[x] for x in bsort]
        result = [0] * len(B)
        i = 0
        j = len(B) - 1
        for x in A:
            if x > B[i]:
                result[bsort[i]] = x
                i += 1
            else:
                result[bsort[j]] = x
                j -= 1
        return result
