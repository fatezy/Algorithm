# # 实现 atoi，将字符串转为整数。
#
#
# 示例 1:
#
# 输入: "42"
# 输出: 42
# 示例 2:
#
# 输入: "   -42"
# 输出: -42
# 解释: 第一个非空白字符为 '-', 它是一个负号。
#      我们尽可能将负号与后面所有连续出现的数字组合起来，最后得到 -42 。
# 示例 3:
#
# 输入: "4193 with words"
# 输出: 4193
# 解释: 转换截止于数字 '3' ，因为它的下一个字符不为数字。
# 示例 4:
#
# 输入: "words and 987"
# 输出: 0
# 解释: 第一个非空字符是 'w', 但它不是数字或正、负号。
#      因此无法执行有效的转换。
# 示例 5:
#
# 输入: "-91283472332"
# 输出: -2147483648
# 解释: 数字 "-91283472332" 超过 32 位有符号整数范围。
#      因此返回 INT_MIN (−231) 。


class Solution:
    def myAtoi(self, str_A):
        """
        :type str: str
        :rtype: int
        """

        if not str_A:
            return 0
        str_A = str_A.strip()
        str_arr = list(str_A)

        res = []
        flag = 1
        for ind,val in enumerate(str_arr):
            if val == '+' and ind == 0:
                flag = 1
                continue
            if val == '-' and ind == 0:
                flag = -1
                continue
            if val in [ str(i) for i in list(range(0,10))]:
                res.append(val)
            else:
                break
        res = ''.join(res)
        if len(res) > 0 and int(res) < 2**31:
            return flag*int(res)
        elif len(res) > 0 and int(res) >= 2**31:
            return flag*2**31 if flag == -1 else flag*2**31-1
        else:
            return 0


    def myAtoi2(self, s):
        """
        :type str: str
        :rtype: int
        """
        ###better to do strip before sanity check (although 8ms slower):
        # ls = list(s.strip())
        # if len(ls) == 0 : return 0
        if len(s) == 0: return 0
        ls = list(s.strip())
        sign = -1 if ls[0] == '-' else 1
        if ls[0] in ['-', '+']: del ls[0]
        ret, i = 0, 0
        while i < len(ls) and ls[i].isdigit():
            ret = ret * 10 + ord(ls[i]) - ord('0')
            i += 1
        return max(-2 ** 31, min(sign * ret, 2 ** 31 - 1))






if __name__ == '__main__':
    print(Solution().myAtoi(" 123"))



