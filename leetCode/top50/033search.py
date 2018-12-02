# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
#
# ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
#
# 搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
#
# 你可以假设数组中不存在重复的元素。
#
# 你的算法时间复杂度必须是 O(log n) 级别。
#
# 示例 1:
#
# 输入: nums = [4,5,6,7,0,1,2], target = 0
# 输出: 4
# 示例 2:
#
# 输入: nums = [4,5,6,7,0,1,2], target = 3
# 输出: -1

class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        for i,val in enumerate(nums):
            if val == target:
                return i
        return -1

    def search2(self,num,target):
        l,r = 0,len(num)-1
        while l<=r:
            mid = (l+r)//2
            if num[mid] == target:
                return mid

            elif num[mid] < num[r]:  # 右半部分有序
                if num[mid] < target and num[r] >= target:
                    l = mid+1
                else:
                    r = mid-1
            else:         # 左半部分有序
                if num[l] <=target and num[mid] >target:
                    r = mid - 1
                else:
                    l = mid + 1

        return -1

if __name__ == '__main__':
    print(Solution().search2([4, 5, 6, 7, 0, 1, 2], 0))