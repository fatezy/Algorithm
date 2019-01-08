# 给定一个非负整数数组，你最初位于数组的第一个位置。
#
# 数组中的每个元素代表你在该位置可以跳跃的最大长度。
#
# 判断你是否能够到达最后一个位置。
#
# 示例 1:
#
# 输入: [2,3,1,1,4]
# 输出: true
# 解释: 从位置 0 到 1 跳 1 步, 然后跳 3 步到达最后一个位置。
# 示例 2:
#
# 输入: [3,2,1,0,4]
# 输出: false
# 解释: 无论怎样，你总会到达索引为 3 的位置。但该位置的最大跳跃长度是 0 ， 所以你永远不可能到达最后一个位置。

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        i = 0
        while i <= len(nums):
            if i+nums[i]>=len(nums)-1:
                return True
            if i == len(nums)-2 or nums[i] == 0:
                return False

            max = nums[i+1]+i+1 # max代表下一步能跳到的最远的位置
            temp = i+1
            if nums[i] != 0:
                for j in range(1,nums[i]+1):
                    if nums[i+j]+i+j >= max:
                        max = nums[i+j]+i+j
                        temp = i + j

            i = temp-1
            i = i+1
        return False

    def canJump2(self, nums):
        """
        高端解法
        :param nums:
        :return:
        """
        stepsLeft = nums[0]

        if not stepsLeft and len(nums) > 1:
            return False

        for num in nums[1:-1]:
            stepsLeft = max(stepsLeft - 1, num)
            if not stepsLeft:
                return False

        return True

if __name__ == '__main__':
    print(Solution().canJump([3, 0, 8, 2, 0, 0, 1]))