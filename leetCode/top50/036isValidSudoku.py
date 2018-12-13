# 判断一个 9x9 的数独是否有效。只需要根据以下规则，验证已经填入的数字是否有效即可。
#
# 数字 1-9 在每一行只能出现一次。
# 数字 1-9 在每一列只能出现一次。
# 数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        if not board:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != '.':
                    if board[i].count(board[i][j]) != 1: # 代表行没有这个元素
                        return False
                    temp = [x[j] for x in board]
                    if temp.count(board[i][j]) != 1:
                        return False

                    for m in range((i//3)*3,(i//3)*3+3):
                        for n in range((j//3)*3,(j//3)*3+3):
                            if i != m and j != n and board[m][n] == board[i][j]:
                                return False
        return True


if __name__ == '__main__':










