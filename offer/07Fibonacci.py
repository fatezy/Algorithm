# -*- coding:utf-8 -*-
# 大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项。
# n<=39
class Solution:
    def Fibonacci(self, n):
        if n is 1:
            return 1
        if n is 2:
            return 1
        return self.Fibonacci(n-1)+self.Fibonacci(n-2)

    def Fibonacci2(self, n):
        count, a, b = 0, 0, 1
        while count < n:
            a, b = b, a + b
            count += 1
        return a







if __name__ == '__main__':
    print(Solution().Fibonacci(10))