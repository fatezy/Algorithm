# -*- coding:utf-8 -*-
# 我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。
# 请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
# 垃圾的牛客网，同样的解法java通过 python不过
class Solution:
    def rectCover(self, number):
        if number is 1:
            return 1
        if number is 2:
            return 2
        return self.rectCover(number - 1) + self.rectCover(number - 2)

    def rectCover2(self, number):
        count, a, b = 0, 0, 1

        if not number:
            return 0

        while count < number:
            count += 1
            a, b = b, a + b
        return b


if __name__ == '__main__':
    print(Solution().rectCover2(2))

