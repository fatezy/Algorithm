# 编写一个程序，通过已填充的空格来解决数独问题。
#
# 一个数独的解法需遵循如下规则：
#
# 数字 1-9 在每一行只能出现一次。
# 数字 1-9 在每一列只能出现一次。
# 数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。


class Solution:
# todo
    def solveSudoku(self, board):
        m = len(board)
        n = len(board) if m else 0
        seen, points =set(), []
        for i in range(m):
            for j in range(n):
                if board[i][j] == '.':
                    points.append((i, j))
                else:
                    seen.update([str(i) + 'r' + board[i][j], str(j) + 'c' + board[i][j], str(i/3) + str(j/3) + board[i][j]])
        def dfs(points, i, board, v):
            if i == len(points): return True
            x, y = points[i]
            for j in range(1, 10):
                tmp = set([str(x) + 'r' + str(j), str(y)+ 'c'+ str(j), str(x/3) + str(y/3) + str(j)])
                if not tmp&v:
                    board[x][y] = str(j)
                    if dfs(points, i + 1, board, v | tmp ): return True
                    board[x][y] = '.'
            return False
        dfs(points, 0, board, seen)