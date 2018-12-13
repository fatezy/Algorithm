# 给定一个二维的矩阵，包含 'X' 和 'O'（字母 O）。
#
# 找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。
#
# 示例:
#
# X X X X
# X O O X
# X X O X
# X O X X
# 运行你的函数后，矩阵变为：
#
# X X X X
# X X X X
# X X X X
# X O X X


class Solution:
    def solve(self,board): #对每个点进行深度搜索
        for i in range(len(board)):
            for j in range(len(board[i])):
                if (i==0 or i == len(board)-1 or j == 0 or j == len(board[i])-1) and board[i][j] == 'O':
                    self.dfs(board,i,j)
        board[:] = [['XO'[c == '$'] for c in row] for row in board]

    def dfs(self,board,i,j):
        if(board[i][j] == 'O'):
            board[i][j] = '$'

        if i>0 and board[i-1][j] == 'O': #上
            self.dfs(board,i-1,j)
        if i<len(board)-1 and board[i+1][j] == 'O': #下
            self.dfs(board,i+1,j)
        if j>0 and board[i][j-1] == 'O':#下
            self.dfs(board,i,j-1)
        if j<len(board[i])-1 and board[i][j+1] == 'O': #下
            self.dfs(board,i+1,j+1)









    def solve2(self, board):
        if not any(board): return

        m, n = len(board), len(board[0])
        save = [ij for k in range(max(m,n)) for ij in ((0, k), (m - 1, k), (k, 0), (k, n - 1))]  #用以保存四条边的位置，是扫面矩阵的四条边，如果有O，则用DFS遍历，
        while save:
            i, j = save.pop()
            if 0 <= i < m and 0 <= j < n and board[i][j] == 'O':
                board[i][j] = 'S'
                save += (i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j) #相当list.append

        board[:] = [['XO'[c == 'S'] for c in row] for row in board]








if __name__ == '__main__':
    board  = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
    Solution().solve(board)




