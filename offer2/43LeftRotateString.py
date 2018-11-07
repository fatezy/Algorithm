# 汇编语言中有一种移位指令叫做循环左移（ROL），现在有个简单的任务，就是用字符串
# 模拟这个指令的运算结果。对于一个给定的字符序列S，请你把其循环左移K位后的序列
# 输出。例如，字符序列S=”abcXYZdef”,要求输出循环左移3位后的结果
# ，即“XYZdefabc”。是不是很简单？OK，搞定它！

class Solution:
    def LeftRotateString(self, s, n):
        if not s:
            return ""

        s = list(s)
        s[0:len(s)-n],s[len(s)-n:len(s)] = s[n:len(s)],s[0:n]

        return "".join(s)


if __name__ == '__main__':
    print(Solution().LeftRotateString("abcXYZdef", 3))