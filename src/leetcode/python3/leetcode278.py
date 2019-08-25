#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    第一个错误版本
"""


def isBadVersion(version):
    pass


# 二分法 48ms
class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1

        start = 0
        end = n

        while start < end:
            mid = (start + end) // 2
            if isBadVersion(mid):
                if isBadVersion(mid - 1):
                    end = mid
                else:
                    return mid
            else:
                if isBadVersion(mid + 1):
                    return mid + 1
                else:
                    start = mid

        return -1


# 48ms
class Solution2:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        start = 1
        end = n

        while start < end:
            mid = (start + end) // 2
            if isBadVersion(mid):
                end = mid
            else:
                start = mid + 1

        return start
