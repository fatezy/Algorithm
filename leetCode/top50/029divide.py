# 给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。
#
# 返回被除数 dividend 除以除数 divisor 得到的商。
#
# 示例 1:
#
# 输入: dividend = 10, divisor = 3
# 输出: 3
# 示例 2:
#
# 输入: dividend = 7, divisor = -3
# 输出: -2

class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """

        res = -1
        if dividend // divisor >= 0:
            res = dividend // divisor
        if dividend // divisor < 0:
            res = -1 * (abs(dividend) // abs(divisor))

        if res >= 2 ** 31:
            return 2 ** 31 - 1
        return res


if __name__ == '__main__':
    print(Solution().divide(7, -3))
    print(abs(7)//abs((-3)))