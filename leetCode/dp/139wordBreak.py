# 给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。
#
# 说明：
#
# 拆分时可以重复使用字典中的单词。
# 你可以假设字典中没有重复的单词。
# 示例 1：
#
# 输入: s = "leetcode", wordDict = ["leet", "code"]
# 输出: true
# 解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。
# 示例 2：
#
# 输入: s = "applepenapple", wordDict = ["apple", "pen"]
# 输出: true
# 解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
#      注意你可以重复使用字典中的单词。
# 示例 3：
#
# 输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# 输出: false
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        self.mem = {}
        return self.helper(s,wordDict)


    def helper(self,s,wordDict):
        if self.mem.__contains__(s):
            return self.mem[s]
        if s in wordDict:
            self.mem[s] = True
            return self.mem[s]
        for i in range(len(s)):
            l = s[0:i]
            r = s[i::]
            # if wordDict.__contains__(r) and self.helper(l,wordDict):    #这样写，效率较高
            #     self.mem[s] = True
            #     return self.mem[s]
            if wordDict.__contains__(l) and self.helper(r,wordDict):
                self.mem[s] = True
                return self.mem[s]



        self.mem[s] = False
        return self.mem[s]


if __name__ == '__main__':
    print(Solution().wordBreak("leetcode",["leet","code"]))




