# 字符序列S=”abcXYZdef”,要求输出循环左移3位后的结果，即“XYZdefabc”。
class Solution:
    def LeftRotateString(self, s, n):
        return s[n:] + s[:n]


if __name__ == '__main__':
    Solution().LeftRotateString('abcdefg',2)