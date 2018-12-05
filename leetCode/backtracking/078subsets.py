# 给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
#
# 说明：解集不能包含重复的子集。
#
# 示例:
#
# 输入: nums = [1,2,3]
# 输出:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]

# 深度优先算法回溯：以【1,2,3】为例
#
# 每轮都传递一个数组起始指针的值，保证遍历顺序：
#
# 第一轮：先遍历以1 开头的所有子集，1→12→123 →13
#
# 第二轮：遍历以2开头的所有子集，2→23
#
# 第三轮:遍历以3开头的所有子集，3
#
# 这样三轮遍历保证能找到全部1开头，2开头，3开头的所有子集；同时，每轮遍历后又把上轮的头元素去掉，这样不会出现重复子集。（包括空集）

class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        # nums.sort()
        self.dfs(res,[],nums,0)
        return res

    def dfs(self,res,temp_list,nums,start):

        res.append(temp_list[:])
        # print(res)
        for i in range(start,len(nums)):
            temp_list.append(nums[i])
            self.dfs(res,temp_list,nums,i+1)
            temp_list.pop()


    def subsets2(self, nums):

        if nums is None:
            return []
        res = []
        self.dfs2(0, sorted(nums), res, [])
        return res

    def dfs2(self,i, nums, res, subres):
        res.append(subres)
        # print(res)
        for j in range(i, len(nums)):
            self.dfs2(j + 1, nums, res, subres + [nums[j]])

    def subsets3(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []

        def dfs(nums, temp, i):
            self.res.append(temp[:])
            for i in range(i, len(nums)):
                temp.append(nums[i])
                dfs(nums, temp, i + 1)
                temp.pop()

        dfs(nums, [], 0)
        return self.res





if __name__ == '__main__':
    print(Solution().subsets2([1, 2, 3]))
    print(Solution().subsets([1, 2, 3]))
    print(Solution().subsets3([1, 2, 3]))




