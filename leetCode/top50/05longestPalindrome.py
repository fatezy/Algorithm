# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为1000。
#
# 示例 1：
#
# 输入: "babad"
# 输出: "bab"
# 注意: "aba"也是一个有效答案。
# 示例 2：
#
# 输入: "cbbd"
# 输出: "bb"


class Solution:
    def longestPalindrome(self, s):

        res = ''
        for i in range(len(s)):
            tmp = self.helper(s,i,i)
            if len(res)<len(tmp):
                res = tmp

            tmp = self.helper(s,i,i+1)
            if len(tmp) > len(res):
                res =tmp
        return res



    def helper(self,s,l,r):
        while l>=0 and r<len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]



if __name__ == '__main__':
    print(Solution().longestPalindrome("babad"))






