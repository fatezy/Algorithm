#
# 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
#
# 说明：本题中，我们将空字符串定义为有效的回文串。
#
# 示例 1:
#
# 输入: "A man, a plan, a canal: Panama"
# 输出: true
# 示例 2:
#
# 输入: "race a car"
# 输出: false


class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = list(filter(lambda x : ('A' <= x <= 'Z') or ('a' <= x <= 'z')or('0' <= x <= '9'), list(s)))
        # newS = [i.lower() for i in s if i.isalnum()]
        # filter,map可以用for in 替代
        s = "".join(s)
        s = s.lower()
        return s[::-1] == s


if __name__ == '__main__':
    print(Solution().isPalindrome("race a car"))