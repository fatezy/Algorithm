# 编写一个程序，通过已填充的空格来解决数独问题。
#
# 一个数独的解法需遵循如下规则：
#
# 数字 1-9 在每一行只能出现一次。
# 数字 1-9 在每一列只能出现一次。
# 数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
# 空白格用 '.' 表示。


class Solution:
    def solveSudoku(self, board):
         self.dfs(board)
         print(board)

    def dfs(self,board):
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == '.':
                    for val in '123456789':
                        board[i][j] = val
                        if self.isValidSudoku(board):
                            if self.dfs(board):
                                return True
                            else:
                                board[i][j] = '.'
                        else:
                            board[i][j] = '.'
                    return False
        return True

    def isValidSudoku(self, board):  # 判断当前的数独是否有效
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        if not board:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != '.':
                    if board[i].count(board[i][j]) != 1:  # 代表行没有这个元素
                        return False
                    temp = [x[j] for x in board]
                    if temp.count(board[i][j]) != 1:
                        return False
                    for m in range((i // 3) * 3, (i // 3) * 3 + 3):
                        for n in range((j // 3) * 3, (j // 3) * 3 + 3):
                            if i != m and j != n and board[m][n] == board[i][j]:
                                return False
        return True

if __name__ == '__main__':
    Solution().solveSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]])
