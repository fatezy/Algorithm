# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
#
# 示例:
#
# 输入: [0,1,0,3,12]
# 输出: [1,3,12,0,0]


class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # for i in range(len(nums)):
        #     if nums[i] == 0:
        #         nums.remove(0)
        #         nums.append(0)
        # return nums

        for i in nums:
            if i == 0:
                nums.remove(0)
                nums.append(0)
        return nums

if __name__ == '__main__':
    print(Solution().moveZeroes([0,1,0,3,12]))