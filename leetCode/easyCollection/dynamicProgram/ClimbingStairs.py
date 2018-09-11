#
# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
#
# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
#
# 注意：给定 n 是一个正整数。
#
# 示例 1：
#
# 输入： 2
# 输出： 2
# 解释： 有两种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶
# 2.  2 阶
# 示例 2：
#

class Solution(object):

    def climbStairs(self, n):
        """
        此方法超时
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        else:
            return Solution().climbStairs(n-1)+Solution().climbStairs(n-2)

    def climbStairs2(self, n):
        a, b = 1, 1
        for i in range(n):
            a, b = b, a + b
        return a

if __name__ == '__main__':
    print(Solution().climbStairs(3))