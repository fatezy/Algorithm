# 给定一个可包含重复数字的序列，返回所有不重复的全排列。
#
# 示例:
#
# 输入: [1,1,2]
# 输出:
# [
#   [1,1,2],
#   [1,2,1],
#   [2,1,1]
# ]

class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        self.helper(res, [], nums, 0,[])
        return res


    def helper(self, res, temp_list, nums, start,index_list):
        if len(temp_list) == len(nums):
            if temp_list not in res:
                res.append(temp_list[:])
            return
        for i in range(len(nums)):
                if i not in index_list:
                    index_list.append(i)
                    temp_list.append(nums[i])
                    self.helper(res, temp_list, nums, i+1,index_list)
                    temp_list.pop()
                    index_list.pop()






if __name__ == '__main__':
    print(Solution().permuteUnique([1, 1, 2]))