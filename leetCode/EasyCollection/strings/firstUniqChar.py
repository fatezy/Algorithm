#   字符串中的第一个唯一字符
# 给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。
#
# 案例:
#
# s = "leetcode"
# 返回 0.
#
# s = "loveleetcode",
# 返回 2.


class Solution:
    def firstUniqChar(self, s):
        """
        第一个独一无二的字母
        :type s: str
        :rtype: int
        """

        hash_map = {}
        for cha in s:
            if cha not in hash_map.keys():
                hash_map[cha] = 1
            else:
                hash_map[cha] += 1

        for i,j in enumerate(s):
            if hash_map[j] == 1:
                return i
        return -1



if __name__ == '__main__':
    print(Solution().firstUniqChar("leetcode"))