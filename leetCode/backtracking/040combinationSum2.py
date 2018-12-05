# 给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
#
# candidates 中的每个数字在每个组合中只能使用一次。
#
# 说明：
#
# 所有数字（包括目标数）都是正整数。
# 解集不能包含重复的组合。
# 示例 1:
#
# 输入: candidates = [10,1,2,7,6,1,5], target = 8,
# 所求解集为:
# [
#   [1, 7],
#   [1, 2, 5],
#   [2, 6],
#   [1, 1, 6]
# ]
# 示例 2:
#
# 输入: candidates = [2,5,2,1,2], target = 5,
# 所求解集为:
# [
#   [1,2,2],
#   [5]
# ]


class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort()          # 目标为8，sort之后可以解决 1,7,1 出现（1,7）（7,1）的问题
        self.helper(candidates,res,[],target,0)
        return res

    def helper(self,candidates,res,temp_list,remain,start):
        if remain < 0:
            return
        elif remain == 0:
            res.append(temp_list[:])
        else:
            for i in range(start,len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                temp_list.append(candidates[i])
                self.helper(candidates,res,temp_list,remain-candidates[i],i+1)
                temp_list.pop()

if __name__ == '__main__':
    print(Solution().combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))


