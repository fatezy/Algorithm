# 将一个字符串转换成一个整数(实现Integer.valueOf(string)的功能，但是string不符合数字要求时返回0)，
# 要求不能使用字符串转换整数的库函数。 数值为0或者字符串不是一个合法的数值则返回0。
# 输入描述:
# 输入一个字符串,包括数字字母符号,可以为空
# 输出描述:
# 如果是合法的数值表达则返回该数字，否则返回0

class Solution:
    def StrToInt(self, s):
        numlist =['0','1','2','3','4','5','6','7','8','9','+','-']
        sum = 0
        label = 1 # 正负数标记
        if s == '':
            return 0
        for c in s:
            if c in numlist:
                if c == '+':
                    label = 1
                    continue
                if c =='-':
                    label = -1
                    continue
                else:
                    sum = sum*10+numlist.index(c)

            if c not in numlist:
                sum = 0
                break
        return label*sum

