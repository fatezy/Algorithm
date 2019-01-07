# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
#
# 示例:
#
# 输入: [-2,1,-3,4,-1,2,1,-5,4],
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = nums[0]
        curr_sum = nums[0]
        for i in range(1,len(nums)):
            curr_sum = nums[i] if curr_sum<=0 else curr_sum+nums[i]
            res = max(curr_sum,res)

        return res


if __name__ == '__main__':
    print(Solution().maxSubArray([1]))
