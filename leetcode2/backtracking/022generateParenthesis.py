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
        """
        :type n: int
        :rtype: List[str]
        """
        if not n:
            return []
        res = []
        temp = ''
        return self.helper(n,0,0,res,'')


    def helper(self,n,l,r,res,temp):
        if len(temp) == 2*n:
            res.append(temp[::])
            return
        if l<n:
            temp +='('
            self.helper(n,l+1,r,res,temp)
            temp = temp[:-1]
        if r<l:
            temp +=')'
            self.helper(n,l,r+1,res,temp)
            temp = temp[:-1]
        return res

if __name__ == '__main__':
    print(Solution().generateParenthesis(3))

