# 将一个字符串转换成一个整数(实现Integer.valueOf(string)的功能，但是string不符合数字要求时返回0)
# ，要求不能使用字符串转换整数的库函数。 数值为0或者字符串不是一个合法的数值则返回0。

class Solution:
    def StrToInt(self, s):
        numlist = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-']
        res = 0
        label = 1
        for i in s:
            if i in numlist:
                if i == '+':
                    label = 1
                    continue
                if i == '-':
                    label = -1
                    continue
                else:
                    res = res*10 + int(i)
            if i not in numlist:
                return 0
        return label*res

