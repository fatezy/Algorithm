# 数组的每个索引做为一个阶梯，第 i个阶梯对应着一个非负数的体力花费值 cost[i](索引从0开始)。
#
# 每当你爬上一个阶梯你都要花费对应的体力花费值，然后你可以选择继续爬一个阶梯或者爬两个阶梯。
#
# 您需要找到达到楼层顶部的最低花费。在开始时，你可以选择从索引为 0 或 1 的元素作为初始阶梯。
#
# 示例 1:
#
# 输入: cost = [10, 15, 20]
# 输出: 15
# 解释: 最低花费是从cost[1]开始，然后走两步即可到阶梯顶，一共花费15。
#  示例 2:
#
# 输入: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
# 输出: 6
# 解释: 最低花费方式是从cost[0]开始，逐个经过那些1，跳过cost[3]，一共花费6。

class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        状态转移方程： dp[i] = min(dp[i- 2] + cost[i - 2], dp[i - 1] + cost[i - 1])
        :type cost: List[int]
        :rtype: int
        """
        if not cost:
            return 0
        if len(cost) == 1:
            return cost[0]
        self.mem = [-1 for i in range(len(cost)+1)]
        self.mem[0],self.mem[1] = 0,0
        return self.helper(cost,len(cost))


    def helper(self,cost,i):
        if self.mem[i] == -1:
            self.mem[i] = min(cost[i-2]+self.helper(cost,i-2),cost[i-1] + self.helper(cost,i-1))
        return self.mem[i]

if __name__ == '__main__':
     Solution().minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])
