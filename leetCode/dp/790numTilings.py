# 有两种形状的瓷砖：一种是
# 2
# x1
# 的多米诺形，另一种是形如
# "L"
# 的托米诺形。两种形状都可以旋转。
#
# XX < - 多米诺
#
# XX < - "L"
# 托米诺
# X
# 给定
# N
# 的值，有多少种方法可以平铺
# 2
# x
# N
# 的面板？返回值
# mod
# 10 ^ 9 + 7。
#
# （平铺指的是每个正方形都必须有瓷砖覆盖。两个平铺不同，当且仅当面板上有四个方向上的相邻单元中的两个，使得恰好有一个平铺有一个瓷砖占据两个正方形。）
#
# 示例:
# 输入: 3
# 输出: 5
# 解释:
# 下面列出了五种不同的方法，不同字母代表不同瓷砖：
# XYZ
# XXZ
# XYY
# XXY
# XYY
# XYZ
# YYZ
# XZZ
# XYY
# XXY
# 提示：
#
# N
# 的范围是[1, 1000]
class Solution(object):
    def numTilings(self, N):
        """
        :type N: int
        :rtype: int
        """
        if not N:
            return 0
        if N == 1:
            return 1
        if N ==2:
            return 2
        if N==3:
            return 5
        self.mem = [-1 for i in range(N)]
        self.mem[0] = 1
        self.mem[1] = 2
        self.mem[2] = 5

        return self.helper(N-1)

    def helper(self,N):
        if self.mem[N] == -1:
            self.mem[N] = (2*self.helper(N-1) +self.helper(N-3)) % ((10**9) + 7)
        return self.mem[N]

if __name__ == '__main__':
    print(Solution().numTilings(1))