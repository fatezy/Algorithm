# Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
#
# You may assume no duplicates in the array.
#
# Example 1:
#
# Input: [1,3,5,6], 5
# Output: 2
# Example 2:
#
# Input: [1,3,5,6], 2
# Output: 1
# Example 3:
#
# Input: [1,3,5,6], 7
# Output: 4
# Example 4:
#
# Input: [1,3,5,6], 0
# Output: 0


# 给你一个有序的list和一个目标值，如果队列中有这个值，返回index,否则
# 返回可以插入的位置

class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: list
        :type target: int
        :rtype: int
        """

        if not  nums:
            return 0
        if target in nums:
            return nums.index(target)
        else:
            nums.append(target)
            nums.sort()
            return nums.index(target)

if __name__ == '__main__':
    print(Solution().searchInsert([1,2,3],4))