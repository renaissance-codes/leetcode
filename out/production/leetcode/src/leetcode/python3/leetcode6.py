#!/usr/bin/env python
# -*- coding:utf-8 -*-


"""
    将z形排序的字符串按照层级输出结果
"""

# 寻找字符串位置的规律，时间复杂度为O(numRows*m) 结果为144ms
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) <= numRows or numRows == 1:
            return s
        result = []
        for i in range(numRows):

            start = 0
            start_s = i

            while start_s < len(s):
                result.append(s[start_s])
                if i == 0 or i == numRows - 1:
                    start_s += (numRows - 1) * 2
                else:
                    if start % 2:
                        start_s += i * 2
                    else:
                        start_s += (numRows - 1 - i) * 2
                start += 1
        return "".join(result)
