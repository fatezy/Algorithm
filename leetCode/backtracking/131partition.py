# 给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。
#
# 返回 s 所有可能的分割方案。
#
# 示例:
#
# 输入: "aab"
# 输出:
# [
#   ["aa","b"],
#   ["a","a","b"]
# ]


class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        self.dfs(s,0,[],res)
        return res

    def dfs(self,s,start,temp_s,res):
        if start == len(s):
            res.append(temp_s[::])

        for i in range(start,len(s)):
            if self.palindrome(s[start:i+1]):   #如果当前截取的为回文字符
                temp_s.append(s[start:i+1])
                self.dfs(s,i+1,temp_s,res)
                temp_s.pop()


    def palindrome(self,s):
        return s[::-1] == s[::]


if __name__ == '__main__':
    print(Solution().partition('aab'))