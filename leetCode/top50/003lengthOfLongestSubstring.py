# 给定一个字符串，找出不含有重复字符的最长子串的长度。

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        res = 0
        str  = "" # 用以记录当前的字符串
        for i in s:
            if i not in str:
                str += i
                if len(str) > res:
                    res = len(str)
            else:
                if len(str) > res:
                    res = len(str)
                str = str[str.find(i) + 1:]
                str += i

        return res

    def lengthOfLongestSubstring2(self, s):
        start = maxLength = 0
        usedChar = {}

        for i in range(len(s)):
            if s[i] in usedChar and start <= usedChar[s[i]]:
                start = usedChar[s[i]] + 1
            else:
                maxLength = max(maxLength, i - start + 1)

            usedChar[s[i]] = i

        return maxLength



if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring("pwwkew"))




