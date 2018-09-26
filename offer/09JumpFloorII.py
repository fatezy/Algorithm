# -*- coding:utf-8 -*-
# 一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。
# 求该青蛙跳上一个n级的台阶总共有多少种跳法。
class Solution:
    def jumpFloorII(self, number):
        if number<=0:
            return 0
        if number is 1:
            return 1
        return 2*self.jumpFloorII(number-1)

    def jumpFloorII2(self,number):
        if not number:
            return 0
        if number is 1:
            return 1
        return 2*self.jumpFloorII2(number-1)
