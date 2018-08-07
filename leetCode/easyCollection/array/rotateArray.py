# 给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums[:k], nums[k:] = nums[len(nums) - k:], nums[:len(nums) - k]
        return nums

if __name__ == '__main__':
    print(Solution().rotate([1, 2, 3, 4], 2))