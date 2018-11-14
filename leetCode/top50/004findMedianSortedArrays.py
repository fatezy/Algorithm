# 给定两个大小为 m 和 n 的有序数组 nums1 和 nums2 。
#
# 请找出这两个有序数组的中位数。要求算法的时间复杂度为 O(log (m+n)) 。
#
# 你可以假设 nums1 和 nums2 不同时为空。


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if not nums1 and not nums2:
            return 0

        new_nums=[] # 用来存储合并的num1和num2

        p1,p2 =0,0  # 分别记录new_nums.nums1,nums2的位置
        while p1<len(nums1) and p2<len(nums2):
            if nums1[p1]>nums2[p2]:
                new_nums.append(nums2[p2])
                p2+=1
            else:
                new_nums.append(nums1[p1])
                p1+=1

        if p1 != len(nums1):
            new_nums.extend(nums1[p1:])
        if p2 != len(nums2):
            new_nums.extend(nums2[p2:])

        if len(new_nums)%2==1:
            return new_nums[int(len(new_nums)/2)]
        else:
            return (new_nums[int(len(new_nums)/2)]+new_nums[int(len(new_nums)/2-1)])/2

if __name__ == '__main__':
    print(Solution().findMedianSortedArrays([1,3],[2]))



