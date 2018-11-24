# 给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。
# #
# # 注意：答案中不可以包含重复的三元组。
# #
# # 例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
# #
# # 满足要求的三元组集合为：
# # [
# #   [-1, 0, 1],
# #   [-1, -1, 2]
# # ]


class Solution:
    # 部分解没有通过
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        num_map = {}
        for i in range(len(nums)):
            if num_map.__contains__(nums[i]):
                num_map[nums[i]] += 1
            else:
                num_map[nums[i]] = 1


        res = []
        for i in range(len(nums)):
            target = 0-nums[i]   # 两数之和目标
            cur_res = []
            for j in range(len(nums)):
                if num_map.__contains__(target- nums[j]):
                    cur_res = [nums[i],nums[j],target-nums[j]]
                    cur_res.sort()
                    if len(set(cur_res)) == 3:
                        if not res.__contains__(cur_res):
                            res.append(cur_res)
                    elif len(set(cur_res)) == 2 and (num_map[nums[j]] >= 2 or num_map[nums[i]] >= 2 or num_map[target-nums[j]] >=2):
                        cur_res.sort()
                        if not res.__contains__(cur_res):
                            res.append(cur_res)
                    elif len(set(cur_res)) == 1 and num_map[nums[i]] >=3:
                        if not res.__contains__(cur_res):
                            res.append(cur_res)

        return res

    def threeSum2(self, nums):
        """超时
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        N, result = len(nums), []
        for i in range(N):
            if i > 0 and nums[i] == nums[i-1]: # 如果两数相等，就跳过
                continue
            target = nums[i]*-1
            s,e = i+1, N-1 # 分别代表从i开始的首尾两端
            while s<e:
                if nums[s]+nums[e] == target: # 等于目标则追加
                    result.append([nums[i], nums[s], nums[e]])
                    s = s+1
                    while s<e and nums[s] == nums[s-1]: # 上面已经s=s+1了，这是为了避免重复
                        s = s+1
                elif nums[s] + nums[e] < target:
                    s = s+1
                else:
                    e = e-1
        return result



if __name__ == '__main__':
    print(Solution().threeSum([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]))








