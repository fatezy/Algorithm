# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
#
# 你可以假设数组中无重复元素。
#
# 示例 1:
#
# 输入: [1,3,5,6], 5
# 输出: 2


class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0
        ind = -1
        for i,val in enumerate(nums):
            if nums[i] == target:
                return i
            if nums[i] < target:
                ind = i
            if nums[i] > target:
                break


        return ind+1

if __name__ == '__main__':
    print(Solution().searchInsert([1,3,5,6], 0))

