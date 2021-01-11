#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
    数字转英文
"""

# 暴力翻译 44ms
class Solution:
    def numberToWords(self, num: int) -> str:
        num1 = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        num2 = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen",
                "Nineteen"]
        num3 = ["Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

        result = ""
        if num == 0:
            return "Zero"
        elif num < 10:
            return num1[num - 1]
        elif num < 20:
            return num2[num - 10]
        elif num < 100:
            t = num // 10
            b = num % 10
            result = num3[t - 2]
            if b:
                result += " " + self.numberToWords(b)
        elif num < 1000:
            t = num // 100
            b = num % 100
            result = num1[t - 1] + " Hundred "
            if b:
                result += self.numberToWords(b)
        elif num < 1000000:
            t = num // 1000
            b = num % 1000
            result = self.numberToWords(t) + " Thousand "
            if b:
                result += self.numberToWords(b)
        elif num < 1000000000:
            t = num // 1000000
            b = num % 1000000
            result = self.numberToWords(t) + " Million "
            if b:
                result += self.numberToWords(b)
        else:
            t = num // 1000000000
            b = num % 1000000000
            result = self.numberToWords(t) + " Billion "
            if b:
                result += self.numberToWords(b)

        return result.strip()


