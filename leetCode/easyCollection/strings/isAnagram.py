# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的一个字母异位词。
#
# 示例 1:
#
# 输入: s = "anagram", t = "nagaram"
# 输出: true
# 示例 2:
#
# 输入: s = "rat", t = "car"
# 输出: false


class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        maps = {}
        mapt = {}
        for c in s:
            maps[c] = maps.get(c,0)+1
        for c in t:
            mapt[c] = mapt.get(c,0)+1
        return maps == mapt