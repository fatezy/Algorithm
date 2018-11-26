# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
# #
# # 有效字符串需满足：
# #
# # 左括号必须用相同类型的右括号闭合。
# # 左括号必须以正确的顺序闭合。
# # 注意空字符串可被认为是有效字符串。

class Solution:
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


if __name__ == '__main__':
    print(Solution().isValid('([)]'))
