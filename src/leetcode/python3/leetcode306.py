#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    累加数
"""


# 深度优先
class Solution:
    def isAdditiveNumber(self, num: str) -> bool:

        def dfs(x, y, ns):
            z = x + y
            sz = str(z)

            if ns[:len(sz)] == sz:
                rests = ns[len(sz):]
                if rests:
                    return dfs(y, z, ns[len(sz):])
                else:
                    return True
            else:
                return False

        slen = len(num)
        if slen < 3:
            return False
        for i in range(slen):
            if num[0] == "0" and i > 0:
                return False
            x = int(num[:i + 1])
            for j in range(i + 1, slen):
                if num[i + 1] == "0" and j - i > 1:
                    break
                y = int(num[i + 1:j + 1])
                if dfs(x, y, num[j + 1:]):
                    return True
        return False
