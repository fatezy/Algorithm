# 题目描述
# 输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
# 例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323
import functools
class Solution:
    def PrintMinNumber(self, numbers):
        # python3 版compare
        if not numbers: return ""

        def cmp(a,b):
            if b+a > a+b:
                return -1
            if a+b < b+a:
                return 1
            return 0


        numbers = list(map(str, numbers))
        numbers = sorted(numbers,key=functools.cmp_to_key(cmp))
        return "".join(numbers).lstrip('0') or'0'


