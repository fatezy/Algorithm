# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
#
# 给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
#
#
#数字代表的字母为手机九宫格的排布
# 示例:
#
# 输入："23"
# 输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        # 递归实现，回溯算法

        mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

        if not digits:
            return []

        if len(digits) == 1:
            return list(mapping[digits[0]])

        prev = self.letterCombinations(digits[:-1])
        additional = mapping[digits[-1]]
        return [s + c for s in prev for c in additional]   #优雅



    # 标准回溯
    def letterCombinations2(self, digits):
        if not digits:
            return []
        dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        res = []
        self.dfs(digits, dic, 0, "", res)
        return res

    def dfs(self, digits, dic, index, path, res):
        if len(path) == len(digits):
            res.append(path)
            return
        for i in range(index, len(digits)):  # 这里和全排列不同
            for j in dic[digits[i]]:
                self.dfs(digits, dic, i + 1, path + j, res)

    # 全排列的回溯
    def permute(self, nums):
        res = []
        self.dfs(nums, [], res)
        return res

    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
            # return # backtracking
        for i in range(len(nums)):
            self.dfs(nums[:i] + nums[i + 1:], path + [nums[i]], res)






if __name__ == '__main__':
    print(Solution().letterCombinations('23'))

