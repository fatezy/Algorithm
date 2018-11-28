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
    def generateParenthesis(self, n):   # 超时
        """
        :type n: int
        :rtype: List[str]
        """
        parenthesis = [ '()'for i in range(n)] #构造全排列对
        parenthesis = "".join(parenthesis)

        res = []
        self.helper(parenthesis,"",res)
        res = list(set(res))
        result = []
        for val in res:
            if self.isValid(val):
                result.append(val)

        return result


    def helper(self,parenthesis,path,res):
        if not parenthesis:
            res.append(path)
        for i in range(len(parenthesis)):
            self.helper(parenthesis[:i]+parenthesis[i+1:],path+parenthesis[i],res)

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        stack_s = []
        parenthess_map = {'[':']','{':'}','(':')'}

        for i in range(len(s)):
            if not stack_s:
                stack_s.append(s[i])
            elif parenthess_map.__contains__(stack_s[-1]) and parenthess_map[stack_s[-1]] == s[i]:
                stack_s.pop()
            else:
                stack_s.append(s[i])


        return True if not stack_s else False

    def generateParenthesis2(self, n):  # 也是回溯，深度优先遍历
        res = []
        self.append(n,0,0,"",res)
        return res

    def append(self,n,left,right,path,res):
        if left==n and right==n:
            res.append(path)
            return
        if left<n:
            self.append(n,left+1,right,path+'(',res)
        if right<n and left>right:
            self.append(n,left,right+1,path+')',res)






if __name__ == '__main__':
    print(Solution().generateParenthesis(3))