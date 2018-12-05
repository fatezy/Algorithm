# 给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
#
# 说明：解集不能包含重复的子集。
#
# 示例:
#
# 输入: [1,2,2]
# 输出:
# [
#   [2],
#   [1],
#   [1,2,2],
#   [2,2],
#   [1,2],
#   []
# ]


class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        self.helper(nums,res,[],0)
        return res


    def helper(self,nums,res,temp_list,start):
        res.append(temp_list[:])
        for i in range(start,len(nums)):
            if i== start or (i != start and nums[i-1] != nums[i]):    # 进行剪枝
                temp_list.append(nums[i])
                self.helper(nums,res,temp_list,i+1)
                temp_list.pop()



if __name__ == '__main__':
    print(Solution().subsetsWithDup([1, 2, 2]))


