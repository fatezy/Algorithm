# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
#
# 给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
#
#
#
# 示例:
#
# 输入："23"
# 输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].


class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}


        if not digits:
            return []

        digits = [i for i in digits]
        res = []
        self.helper(digits,'',res,mapping,0)

        return res

    def helper(self,digits,temp_s,res,mapping,start):
        if len(temp_s) == len(digits):
            res.append(temp_s[::])
            return

        for i in range(start,len(digits)):
            for j in mapping[digits[i]]:
                temp_s += j
                self.helper(digits,temp_s,res,mapping,i+1)
                temp_s = temp_s[:-1]



if __name__ == '__main__':
    print(Solution().letterCombinations('23'))