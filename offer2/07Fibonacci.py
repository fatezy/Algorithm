# 大家都知道斐波那契数列，现在要求输入一个整数n，
# 请你输出斐波那契数列的第n项（从0开始，第0项为0）。


class Solution:
    def Fibonacci(self, n):
        a,b = 0,1
        for i in range(n):
            a,b = b,a+b
        return a



if __name__ == '__main__':
    print(11)
    print(Solution().Fibonacci(3))