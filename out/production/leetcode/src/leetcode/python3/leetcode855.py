#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    考试就座
"""


class ExamRoom:

    def __init__(self, N: int):
        self.num = N
        self.seats = []

    def seat(self) -> int:
        if self.seats:
            res = -1
            ind = -1
            ins = -1
            if self.seats[0] != 0:
                v = self.seats[0] - 1
                res = v
                ind = 0
                ins = 0

            for i in range(1, len(self.seats)):
                vi = (self.seats[i] + self.seats[i - 1]) >> 1
                dis = vi - self.seats[i - 1] - 1
                if dis > res:
                    res = dis
                    ind = i
                    ins = vi
            if self.seats[-1] != self.num - 1:
                v = self.num - self.seats[-1] - 2
                if v > res:
                    ind = len(self.seats)
                    ins = self.num - 1
            self.seats.insert(ind, ins)

            return ins

        else:
            self.seats.append(0)
            return 0

    def leave(self, p: int) -> None:
        ind = self.seats.index(p)
        self.seats.pop(ind)


class Node:

    def __init__(self, val):
        self.val = val
        self.next = None


# 链表实现
class ExamRoom2:

    def __init__(self, N: int):
        self.num = N
        self.seats = None

    def seat(self) -> int:

        if self.seats is None:
            self.seats = Node(0)
            return 0
        else:

            root = self.seats

            ind = -1
            res = -1
            node = None
            if root.val != 0:
                ind = 0
                res = root.val
                node = Node(0)

            while root and root.next:
                tind = (root.next.val + root.val) >> 1
                tres = tind - root.val
                if tres > res:
                    node = root
                    res = tres
                    ind = tind
                root = root.next
            if root.val != self.num - 1:
                eres = self.num - 1 - root.val
                if eres > res:
                    ind = self.num - 1
                    node = root
                    res = eres
            # print(res, ind)
            if ind == 0:
                node.next = self.seats
                self.seats = node
            else:
                vnode = Node(ind)
                nn = node.next
                node.next = vnode
                vnode.next = nn
            return ind

    def leave(self, p: int) -> None:
        root = self.seats
        hroot = Node(-1)
        hroot.next = root
        lroot = hroot
        while root:
            if root.val == p:
                lroot.next = root.next
                break
            else:
                root = root.next
                lroot = lroot.next
        self.seats = hroot.next