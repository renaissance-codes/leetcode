#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    UTF-8编码验证
"""
from typing import List


# 分别判断
class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        d_len = len(data)

        i = 0
        while i < d_len:
            d = data[i]

            if d >> 7 == 0:
                i += 1
            elif d >> 5 == 6:
                if i + 1 < d_len and data[i + 1] >> 6 == 2:
                    i += 2
                else:
                    return False
            elif d >> 4 == 14:
                if i + 2 < d_len and data[i + 1] >> 6 == 2 and data[i + 2] >> 6 == 2:
                    i += 3
                else:
                    return False
            elif d >> 3 == 30:
                if i + 3 < d_len and data[i + 1] >> 6 == 2 and data[i + 2] >> 6 == 2 and data[i + 3] >> 6 == 2:
                    i += 4
                else:
                    return False
            else:
                return False

        return True

# 简洁写法
class Solution2:
    def validUtf8(self, data: List[int]) -> bool:
        d_len = len(data)

        d = 0
        for x in data:
            mask = 1 << 7
            if d == 0:
                while mask & x:
                    mask >>= 1
                    d += 1
                if d == 0:
                    continue

                if d in {2, 3, 4}:
                    d -= 1
                else:
                    return False
            else:
                if x >> 6 == 2:
                    d -= 1
                else:
                    return False
        if d:
            return False

        return True