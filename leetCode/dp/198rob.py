# 你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
#
# 给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。
#
# 示例 1:
#
# 输入: [1,2,3,1]
# 输出: 4
# 解释: 偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
#      偷窃到的最高金额 = 1 + 3 = 4 。
# 示例 2:
#
# 输入: [2,7,9,3,1]
# 输出: 12
# 解释: 偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
#      偷窃到的最高金额 = 2 + 9 + 1 = 12 。

class Solution(object):
    def rob(self, nums):
        """ 记忆化递归法
        状态转移方程 dp[i] = max(num[i] + dp[i - 2], dp[i - 1])
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        self.mem = [-1 for i in range(len(nums))]
        self.mem[0] = nums[0]
        self.mem[1] = max(nums[0],nums[1])
        return self.helper(nums,len(nums)-1)


    def helper(self,nums,i):
        if self.mem[i] == -1:
            self.mem[i] = max(nums[i]+self.helper(nums,i-2),self.helper(nums,i-1))
        return self.mem[i]

    def rob2(self,nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp = [-1 for i in range(len(nums))]
        dp[0],dp[1] = nums[0],max(nums[0],nums[1])
        for i in range(len(nums)):
            if dp[i] == -1:
                dp[i] = max(nums[i]+dp[i-2],dp[i-1])
        return dp[-1]

if __name__ == '__main__':
    print(Solution().rob2([1, 2, 3, 1]))