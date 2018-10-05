# 题目描述
# 在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,
# 并返回它的位置, 如果没有则返回 -1（需要区分大小写）.
class Solution:
    def FirstNotRepeatingChar(self, s):
        char_map = {}
        seq = []
        for i in s:
            if char_map.__contains__(i):
                char_map[i] += 1
            else:
                char_map[i] = 1
                seq.append(i)

        for key in seq:
            if char_map[key] == 1:
                return s.find(key)

        return -1


if __name__ == '__main__':
    print(Solution().FirstNotRepeatingChar('google'))