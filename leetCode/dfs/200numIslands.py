# 给定一个由 '1'（陆地）和 '0'（水）组成的的二维网格，计算岛屿的数量。一个岛被水包围，
# 并且它是通过水平方向或垂直方向上相邻的陆地连接而成的。你可以假设网格的四个边均被水包围。
#
# 示例 1:
#
# 输入:
# 11110
# 11010
# 11000
# 00000
#
# 输出: 1
# 示例 2:
#
# 输入:
# 11000
# 11000
# 00100
# 00011
#
# 输出: 3


class Solution(object):
    # 典型的深度搜索问题，类似于130题，每次深度搜索将可以搜索
    # 到为1的全部重置为0，岛屿数加一
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    self.helper(grid,i,j)
                    res += 1
        return res

    def helper(self,grid,i,j):
        if grid[i][j] == '1':
            grid[i][j] = '0'

        if i>0 and grid[i-1][j] == '1': #上
            self.helper(grid,i-1,j)

        if i<len(grid)-1 and grid[i+1][j] == '1':  # 下
            self.helper(grid,i+1,j)

        if j<len(grid[i])-1 and grid[i][j+1] == '1':  # 右
            self.helper(grid,i,j+1)

        if j >0 and grid[i][j-1] == '1':  # 左
            self.helper(grid, i, j-1)


if __name__ == '__main__':
    grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
    print(Solution().numIslands(grid))