# 题目描述
# 定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小
# 元素的min函数（时间复杂度应为O（1））。


# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.li =[]

    def push(self, node):
        self.li.append(node)

    def pop(self):
        self.li.pop()

    def top(self):
       return self.li[-1]

    def min(self):
        return min(self.li)