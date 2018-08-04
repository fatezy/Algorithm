# 给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        temp = 0
        for i in range(len(nums)):
            if nums[i] != nums[temp]:
                temp += 1
                nums[temp] = nums[i]
        return temp+1


if __name__ == '__main__':
    print(Solution().removeDuplicates([1, 1, 2, 3]))
