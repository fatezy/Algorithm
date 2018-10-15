# 输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示


class Solution:
    def NumberOf1(self, n):
        count = 0
        if n < 0:
            n = n & 0xffffffff  # python无限精度，需加以处理
        while n:
            count += 1
            n = (n - 1) & n
        return count