# 罗马数字包含以下七种字符: I， V， X， L，C，D 和 M。
#
# 字符          数值
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# 例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。

class Solution:
    def romanToInt(self, s):

        romans = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}

        prev_value = running_total = 0

        for i in range(len(s) - 1, -1, -1):
            int_val = romans[s[i]]
            if int_val < prev_value:
                running_total -= int_val
            else:
                running_total += int_val
            prev_value = int_val

        return running_total
