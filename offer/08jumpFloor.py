# -*- coding:utf-8 -*-
# 一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
class Solution:
    def jumpFloor(self, number):
        if number is 1:
            return 1
        if number is 2:
            return 2
        return self.jumpFloor(number-1)+self.jumpFloor(number-2)

    def jumpFloor2(self, number):
        count, a, b = 0, 0, 1
        while count < number:
            a, b = b, a + b
            count += 1
        return b

    def jumpFloor3(self,number):
        count,a,b = 0,0,1

        while count < number:
            count = count + 1
            a ,b = b,a+b
        return b


if __name__ == '__main__':
    print(Solution().jumpFloor3(5))