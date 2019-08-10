#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

"""
    行星碰撞    
"""


# 暴力求解 292ms
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        tasteroids = asteroids
        result = []
        change = True
        while change:
            for x in tasteroids:
                if len(result) == 0:
                    result.append(x)
                else:
                    p = result.pop()
                    if p > 0 and x < 0:
                        if p > -x:
                            result.append(p)
                        elif p < -x:
                            result.append(x)
                    else:
                        result.append(p)
                        result.append(x)
            if len(result) < len(tasteroids):
                tasteroids = result
                result = []
            else:
                change = False

        return result

# 循环的位置不同
class Solution2:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        result = []

        for x in asteroids:
            while len(result) and result[-1] > 0 and x < 0:
                p = result.pop()
                if p > -x:
                    x = p
                elif p == -x:
                    break
            else:
                result.append(x)

        return result
