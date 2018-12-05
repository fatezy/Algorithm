# 给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
#
# candidates 中的数字可以无限制重复被选取。
#
# 说明：
#
# 所有数字（包括 target）都是正整数。
# 解集不能包含重复的组合。
# 示例 1:
#
# 输入: candidates = [2,3,6,7], target = 7,
# 所求解集为:
# [
#   [7],
#   [2,2,3]
# ]
# 示例 2:
#
# 输入: candidates = [2,3,5], target = 8,
# 所求解集为:
# [
#   [2,2,2,2],
#   [2,3,3],
#   [3,5]
# ]


class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        self.helper(candidates,res,[],target,0)
        return res

    def helper(self,candidates,res,temp_list,remain,start):
        if remain < 0:
            return
        elif remain == 0:
            res.append(temp_list[:])
        else:
            for i in range(start,len(candidates)):
                temp_list.append(candidates[i])
                self.helper(candidates,res,temp_list,remain-candidates[i],i)
                temp_list.pop()



if __name__ == '__main__':
    print(Solution().combinationSum([2, 3, 6, 7], 7))
