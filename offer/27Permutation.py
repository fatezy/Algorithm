# 输入一个字符串,按字典序打印出该字符串中字符的所有排列。例如输入字符串abc,
# 则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。

#全排列问题

# -*- coding:utf-8 -*-
class Solution:
    def Permutation(self, ss):
        if ss is None or len(ss) < 2:
            return ss
        ss = list(ss)
        res = set({})
        self.permut(ss, 0, res)

        return sorted(list(res))

    def permut(self, ss, begin, res):
        if begin == len(ss) - 1:
            res.add(''.join(ss))
            return

        cur = begin
        for cur in range(begin, len(ss)):
            self.swap(ss, begin, cur)    # 交换
            self.permut(ss, begin+1, res)
            self.swap(ss, begin, cur)    # 复位

    def swap(self, ss, i, j):
        ss[i], ss[j] = ss[j], ss[i]
