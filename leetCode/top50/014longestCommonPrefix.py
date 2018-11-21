# 编写一个函数来查找字符串数组中的最长公共前缀。
#
# 如果不存在公共前缀，返回空字符串 ""。
#
# 示例 1:
#
# 输入: ["flower","flow","flight"]
# 输出: "fl"
# 示例 2:
#
# 输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。

class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        # 快不快不重要，要优雅^-^
        if not strs:
            return ""

        for i, letter_group in enumerate(zip(*strs)):   # *所有的数据
            if len(set(letter_group)) > 1: #最多只能有一个，共同的数
                return strs[0][:i]
        else:
            return min(strs)

    def longestCommonPrefix2(self,strs):
        if not strs:
            return ""

        min_length = 2**31
        for i in strs:
            if len(i) < min_length:
                min_length = len(i)

        res  = ""
        for i in range(min_length):
            val = strs[0][i]
            for j in strs:
                if val != j[i]:
                    return res
            res += val

        return res






if __name__ == '__main__':
    print(Solution().longestCommonPrefix2(["flower", "flow", "flight"]))