# n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
#
#
#
# 上图为 8 皇后问题的一种解法。
#
# 给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。
#
# 每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。
#
# 示例:
#
# 输入: 4
# 输出: [
#  [".Q..",  // 解法 1
#   "...Q",
#   "Q...",
#   "..Q."],
#
#  ["..Q.",  // 解法 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]


class Solution:

    # def solveNQueens(self,n):



    def solveNQueens2(self, n):
        res = []
        self.dfs([-1] * n, 0, [], res)
        return res

    # nums is a one-dimension array, like [1, 3, 0, 2] means
    # first queen is placed in column 1, second queen is placed
    # in column 3, etc.
    def dfs(self, nums, index, path, res):
        if index == len(nums):       # index 代表是处理的第几行的皇后位置
            res.append(path)
            return  # backtracking
        for i in range(len(nums)):
            nums[index] = i
            if self.valid(nums, index):  # pruning
                tmp = "." * len(nums) # temp初始化为 '.'
                self.dfs(nums, index + 1, path + [tmp[:i] + "Q" + tmp[i + 1:]], res)

    # check whether nth queen can be placed in that column
    def valid(self, nums, n):
        for i in range(n):
            if abs(nums[i] - nums[n]) == n - i or nums[i] == nums[n]:# 前一个检测是否是45度
                return False
        return True


if __name__ == '__main__':
    print(Solution().solveNQueens2(4))