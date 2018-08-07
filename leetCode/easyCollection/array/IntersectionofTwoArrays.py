# 给定两个数组，写一个方法来计算它们的交集。
#
# 例如:
# 给定 nums1 = [1, 2, 2, 1], nums2 = [2, 2], 返回 [2, 2].


class Solution:

    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dict1 = dict()
        for i in nums1:
            if i not in dict1:
                dict1[i] = 1
            else:
                dict1[i] += 1
        ret = []
        for i in nums2:
            if i in dict1 and dict1[i] > 0:
                ret.append(i)
                dict1[i] -= 1
        return ret


if __name__ == '__main__':
    print(Solution().intersect([11, 2, 2, 1], [1, 2]))