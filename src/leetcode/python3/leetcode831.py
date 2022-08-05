#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    隐藏个人信息
"""


class Solution:
    def maskPII(self, S: str) -> str:
        if "@" in S:
            sarray = S.split("@")
            firstname = sarray[0].lower()
            lastname = sarray[1].lower()

            return firstname[0] + "*****" + firstname[-1] + "@" + lastname
        else:
            nums = []
            for s in S:
                if s.isdigit():
                    nums.append(s)
            if len(nums) == 10:
                return "***-***-" + "".join(nums[-4:])
            else:
                return "+" + "*" * (len(nums) - 10) + "-***-***-" + "".join(nums[-4:])
