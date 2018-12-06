# 给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。
#
# 例如，给出 n = 3，生成结果为：
#
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]


class Solution:
    def generateParenthesis(self, n):
        res = []
        self.helper(n,0,0,res,'')
        return res


    def helper(self,n,left,right,res,temp_s):
        if len(temp_s) == 2*n:
            res.append(temp_s[::])
            return
        if left<=n:
            if left<n:
                temp_s += '('
                self.helper(n,left+1,right,res,temp_s)
                temp_s = temp_s[:-1]
            if right<left:
                temp_s += ')'
                self.helper(n,left,right+1,res,temp_s)
                temp_s = temp_s[:-1]



if __name__ == '__main__':
    print(Solution().generateParenthesis(3))





